# aiogram import
from aiogram import types

# kode import
from services.services import get_seasons_by_movie_code
from utils import texts, buttons



async def handle_seasons(message: types.Message, title: str, movie_file_url: str, code: str):

    """
    Kinolarga va qismlarga fasl berilganmi yoqmi tekshirish va tugma ko'rinishida chiqarish
    """

    seasons_data = get_seasons_by_movie_code(code)
    print(seasons_data)

    if seasons_data:
        keyboard = types.InlineKeyboardMarkup()
        season_ids = set()
        for season in seasons_data:
            season_id = season.get('id')
            if season_id and season_id not in season_ids:
                season_title = season.get('title', 'Unknown Season')
                keyboard.add(types.InlineKeyboardButton(text=f"{season_title}", callback_data=f"season_{season_id}_{code}"))
                season_ids.add(season_id)
        await message.answer(f"Please select a season for {title}:", reply_markup=keyboard)
    else:
        await message.answer_video(
            video=movie_file_url,
            caption=texts.MOVIES_SEND(
                title=title,
                year='Unknown Year',
                language='Unknown Language',
                quality='Unknown Quality',
                country='Unknown Country',
                genre='Unknown Genre',
                download_count='Unknown Count'
            ),
            reply_markup=buttons.create_movie_buttons()
        )
