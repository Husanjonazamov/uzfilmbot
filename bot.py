from aiogram import executor

from loader import dp, bot
from utils.env import ADMIN

import handler


async def on_startup(dp):
    """
    botni asosiy ishga tushiradigan file
    """
    
    await bot.send_message(ADMIN, 'bot ishga tushdi')
    
    
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)