# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext

# kode import
from services.services import get_movies_by_category
from utils import buttons, texts
from loader import dp, bot

# add import
from asyncio import create_task




async def show_movies_by_category_task(callback_query: types.CallbackQuery, state: FSMContext):

    """
    Categoryaga mansub kinolar ro'yhati
    """

    category_title = callback_query.data.split('_')[1]
    movies = get_movies_by_category(category_title)

    if movies:
        response = ''
        for index, movie in enumerate(movies, start=1):
            title = category_title
            year = movie.year
            code = movie.code
            response += texts.get_response(
                index=index,
                title=title,
                year=year,
                code=code
            )
        await callback_query.message.answer(response, reply_markup=buttons.delete_message())
    else:
        await callback_query.message.answer(texts.CATEGORY_NOT_MOVIES, reply_markup=buttons.delete_message())


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('category_'), state='*')
async def show_movies_by_category(callback_query: types.CallbackQuery, state: FSMContext):
    await create_task(show_movies_by_category_task(callback_query, state))
