# aiogram import
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp, bot
from services.services import get_movie_by_list
from handler.movies.movies_download.app import app
from utils import buttons, texts

# add import
from asyncio import create_task



async def movies_list_task(client, message: types.Message, state: FSMContext):

    """
    Ishlatilmaydi
    """

    movies = get_movie_by_list()

    if movies:
        response_text = ""
        for movie in movies:
            title = movie.get('title')
            code = movie.get('code')

            response_text += texts.MOVIES_LIST_SEND(
                title=title,
                code=code
            )
        await message.answer(
            text=response_text
        )
    else:
        await message.answer(texts.KOD_IS_NOT)



@dp.message_handler(commands=['list'], state='*')
async def movies_list(message: Message, state: FSMContext):
    create_task(movies_list_task(app, message, state))

@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.MOVIES_LIST,
                )), state="*", content_types=['text'])
async def movies_list(message: Message, state: FSMContext):
    create_task(movies_list_task(app, message, state))
