# aiogram import
from aiogram import types

# kode import
from utils import texts, buttons
from handler.movies.movies_download.download_count import update_download_count_view
from services.services import get_season_movies_and_episodes

# add import


async def send_episodes(message: types.Message, code: str, season_id=None):
    """
    Kinoga tegishli bo'lgan qismlarni yoki to'g'ridan-to'g'ri kinoni yuboradigan funksiya
    """

    episodes_data = None

    if season_id:
        try:
            episodes_data = get_season_movies_and_episodes(season_id=season_id)
        except:
            await message.answer(texts.MOVIE_NOT_FOUND)
            return
    else:
        try:
            episodes_data = get_season_movies_and_episodes(season_id=season_id)
        except:
            return

    if not episodes_data:
        episode_download_count = await update_download_count_view(code)
        if episode_download_count is None:
            await message.answer(texts.MOVIE_NOT_FOUND)
            return
        
        movie_caption = texts.MOVIE_DOWNLOAD_COUNT.format(download_count=episode_download_count)
        await message.answer(texts.MOVIE_NOT_FOUND)
        return

    for episode in episodes_data:
        episode_title = episode.get('title')
        episode_year = episode.get('year')
        episode_language = episode.get('language')
        episode_quality = episode.get('quality')
        episode_country = episode.get('country')
        episode_genre = episode.get('genre')
        episode_file_id = episode.get('file_id')
        episode_number = episode.get('episode_number')
        episode_download_count = await update_download_count_view(code)

        if episode_download_count is None:
            await message.answer(texts.MOVIE_NOT_FOUND)
            return

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
