# aiogram import
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

# kode import
from loader import dp, bot
from handler.movies.movies_download.app import app
from utils import buttons, texts
from services.services import get_category_by_list

from asyncio import create_task




async def send_category_task(client, message: types.Message, state: FSMContext):

    """
    Modeldan kelayotgan categoryani button ko'rinishida yuboardigan funksiya
    """

    categories = get_category_by_list()
    if categories:
        keyboard = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(text=category.title, callback_data=f"category_{category.title}") for category
                   in categories]
        for i in range(0, len(buttons), 2):
            keyboard.row(*buttons[i:i + 2])
        await message.answer(texts.CATEGORY_SELECT, reply_markup=keyboard)
    else:
        await message.answer(texts.CATEGORY_ERROR)





@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.MOVIES_LIST,
                )), state="*", content_types=['text'])
async def movies_list(message: Message, state: FSMContext):
    await create_task(send_category_task(app, message, state))


@dp.message_handler(commands=['list'], state='*')
async def movies_list(message: Message, state: FSMContext):
    await create_task(send_category_task(app, message, state))