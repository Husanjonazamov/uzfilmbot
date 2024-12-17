# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor

# kode import
from loader import dp
from handler.movies.serials.episode_handler import handle_episodes



@dp.callback_query_handler(lambda c: c.data.startswith('season_'))
async def process_season_callback(callback_query: types.CallbackQuery, state: FSMContext):

    """
    Fasl bo'yicha kinnoni yuklab olish funksiyasi (button bosilganda)
    """

    data = callback_query.data.split('_')
    season_id = int(data[1])
    code = data[2]

    await handle_episodes(callback_query.message, code, season_id)
