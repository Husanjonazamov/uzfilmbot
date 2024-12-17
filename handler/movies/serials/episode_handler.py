# aiogram import
from aiogram import types

# kode import
from services.services import get_season_movies_and_episodes
from handler.movies.movies_download.download_count import update_download_count_view
from handler.users.subscription import check_subscriptions
from utils import texts, buttons
from loader import bot




async def handle_episodes(message: types.Message, code: str, season_id: str):

    """
    Asosiy qismlarni olish funksiyasi
    """

    # Sezondagi film va epizodlarni olish
    season_data = get_season_movies_and_episodes(season_id, code)
    user_id = message.from_user.id

    if season_data:
        not_subscribed = await check_subscriptions(bot, user_id)
        if not_subscribed:
            keyboard = buttons.get_subscription_buttons(not_subscribed)
            await message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)
            return
        
        # Filmlar ro'yxati
        movies = season_data.get('movies', [])
        episodes = season_data.get('episodes', [])
        
        if movies:
            movie_data = movies[0] 
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
        
        # Epizodlarni ko'rsatish
        if episodes:
            for episode in episodes:
                episode_title = episode.get('title')
                episode_year = episode.get('year')
                episode_language = episode.get('language')
                episode_quality = episode.get('quality')
                episode_country = episode.get('country')
                episode_genre = episode.get('genre')
                episode_file_id = episode.get('file_id')
                episode_number = episode.get('episode_number')
                episode_download_count = await update_download_count_view(code)

                if episode_file_id:
                    episode_caption = texts.EPISODE(
                        episode_title=episode_title,
                        episode_year=episode_year,
                        episode_language=episode_language,
                        episode_quality=episode_quality,
                        episode_country=episode_country,
                        episode_genre=episode_genre,
                        episode_number=episode_number,
                        episode_download_count=episode_download_count
                    )

                    await message.answer_video(
                        video=episode_file_id,
                        caption=episode_caption,
                        reply_markup=buttons.create_movie_buttons()
                    )
        else:
            await message.reply("No episodes found in this season.")
    else:   
        await message.answer(texts.NO_SEASON_SELECTED)
