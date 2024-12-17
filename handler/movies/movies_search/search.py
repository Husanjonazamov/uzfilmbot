# aiogram import
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

# kode import
from loader import dp
from utils.state import MoviesSearch
from utils import buttons, texts
from services.services import get_search_movie

# add import
import logging
from asyncio import create_task



async def search_movies_task(message: Message, state: FSMContext):

    """
    Chiqgan natijani button ko'rinishida foydalanuvchiga yuborish
    """

    query = message.text.strip()
    movies = get_search_movie(query)

    if movies:
        response = "Natijalar:\n"
        keyboard = InlineKeyboardMarkup(row_width=1)
        for index, movie in enumerate(movies, start=1):
            button_text = f"🎬 {movie.title}"
            button_callback_data = f"{movie.code}" 
            keyboard.add(InlineKeyboardButton(text=button_text, callback_data=button_callback_data))
            response += f"{index}. {movie.title} - Kodi: {movie.code}\n\n"

        await message.answer(response, reply_markup=keyboard)
    else:
        await message.answer(texts.SEARCH_NOT_FOUND)
        await state.set_state(MoviesSearch.waiting_for_query)



@dp.message_handler(state=MoviesSearch.waiting_for_query, content_types=['text'])
async def search_movies(message: Message, state: FSMContext):
    text = message.text
    if text == buttons.BACK_TEXT:
        await state.finish()
        await message.answer(texts.MAIN_MENU, reply_markup=buttons.MAIN_MENU)
    else:
        await create_task(search_movies_task(message, state))
