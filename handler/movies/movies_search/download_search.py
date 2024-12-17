# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext

# kode import
from handler.movies.movies_download.download_count import update_download_count_view
from loader import dp, bot
from services.services import get_movie_by_code, get_episodes_by_series_code
from utils.state import MoviesSearch
from handler.users.subscription import check_subscriptions
from utils import texts, buttons

# add import
from asyncio import create_task




async def download_movie_task(callback_query: types.CallbackQuery, state: FSMContext):

    """
    qidirish natijasida chiqgan kinolarni yuklab olish funksiyasi
    """

    code = callback_query.data

    movie_data = get_movie_by_code(code)
    user_id = callback_query.message.from_user.id

    not_subscribed = await check_subscriptions(bot, user_id)


    if not_subscribed:
        keyboard = buttons.get_subscription_buttons(not_subscribed)
        await callback_query.message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)
    else:
        if movie_data:
            movie_file_url = movie_data.get('file_id')
            title = movie_data.get('title')
            year = movie_data.get('year')
            language = movie_data.get('language')
            quality = movie_data.get('quality')
            country = movie_data.get('country')
            genre = movie_data.get('genre')

            download_count = await update_download_count_view(code)

            caption_text = texts.MOVIES_SEND(
                title=title,
                year=year,
                language=language,
                quality=quality,
                country=country,
                genre=genre,
                download_count=download_count
            )

            await callback_query.message.answer_video(
                video=movie_file_url,
                caption=caption_text,
                reply_markup=buttons.create_movie_buttons()
            )


            episodes_data = get_episodes_by_series_code(code)
            

            for episode in episodes_data:
                episode_title = episode['title']
                episode_year = episode['year']
                episode_language = episode['language']
                episode_quality = episode['quality']
                episode_country = episode['country']
                episode_genre = episode['genre']
                episode_file_id = episode['file_id']
                episode_number = episode['episode_number']
                episode_download_count = await update_download_count_view(code)

                if download_count is None:
                    await callback_query.message.reply("Movie not found in the database.")
                    return

                episode = texts.EPISODE(
                    episode_title=episode_title,
                    episode_year=episode_year,
                    episode_language=episode_language,
                    episode_quality=episode_quality,
                    episode_country=episode_country,
                    episode_genre=episode_genre,
                    episode_number=episode_number,
                    episode_download_count=episode_download_count
                )

                await callback_query.message.answer_video(
                    video=episode_file_id,
                    caption=episode,
                    reply_markup=buttons.create_movie_buttons()
                )


        else:
            await callback_query.message.answer(texts.KOD_IS_NOT)
            
    await MoviesSearch.waiting_for_query.set()


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.isdigit(), state="*")
async def download_movie(callback_query: types.CallbackQuery, state: FSMContext):
    await create_task(download_movie_task(callback_query, state))