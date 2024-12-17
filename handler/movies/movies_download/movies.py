# aiogram import
from aiogram import types

# kode import
from loader import dp, bot
from handler.movies.movies_download.app import app
from services.services import get_movie_by_code, get_seasons_by_movie_code
from handler.users.subscription import check_subscriptions
from utils import texts, buttons
from handler.movies.movies_download.download_count import update_download_count_view
from handler.movies.serials.season import handle_seasons
from handler.movies.serials.episode import send_episodes

# add import
from asyncio import create_task


async def movies_task(client, message: types.Message):

    """
    Kinoni tashlab beradigan asosiy funksiya
    """

    code = message.text.strip()
    movie_data = get_movie_by_code(code)
    user_id = message.from_user.id

    not_subscribed = await check_subscriptions(bot, user_id)

    if not_subscribed:
        keyboard = buttons.get_subscription_buttons(not_subscribed)
        await message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)
    else:
        if movie_data:
            movie_file_url = movie_data.get('file_id')

            if not movie_file_url:
                await message.reply("Movie file URL is invalid.")
                return

            title = movie_data.get('title')
            year = movie_data.get('year')
            language = movie_data.get('language')
            quality = movie_data.get('quality')
            country = movie_data.get('country')
            genre = movie_data.get('genre')

            download_count = await update_download_count_view(code)

            if download_count is None:
                await message.reply("Movie not found in the database.")
                return

            seasons_data = get_seasons_by_movie_code(code)

            if seasons_data:
                await handle_seasons(message, title, movie_file_url, code)
            else:
                caption_text = texts.MOVIES_SEND(
                    title=title,
                    year=year,
                    language=language,
                    quality=quality,
                    country=country,
                    genre=genre,
                    download_count=download_count
                )

                await message.answer_video(
                    video=movie_file_url,
                    caption=caption_text,
                    reply_markup=buttons.create_movie_buttons()
                )

                await send_episodes(message, code)
        else:
            await message.answer(texts.KOD_IS_NOT)

@dp.message_handler(lambda message: message.text.isdigit(), content_types=['text'])
async def handle_message(message: types.Message):
    await create_task(movies_task(app, message))
