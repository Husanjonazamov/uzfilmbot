# aiogram import
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# add import
from utils.env import BOT_TOKEN
import logging


storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)