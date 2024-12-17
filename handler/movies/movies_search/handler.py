# aiogram import
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp
from utils.state import MoviesSearch
from utils import texts, buttons

# add import
from asyncio import create_task



async def search_start(message: Message, state: FSMContext):

    """
    Qidirish ni boshlash funksiyasi
    """

    await message.answer(texts.MOVIES_SEARCH, reply_markup=buttons.BACK)
    await MoviesSearch.waiting_for_query.set()


@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.SEARCH,
                )), state="*", content_types=['text'])
async def search(message: Message, state: FSMContext):
  create_task(search_start(message, state))