# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from services.services import createUser, getUser



@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    
    get_user = getUser(user_id)
    user = {'user_id': user_id}
    
    
    if not get_user:
        createUser(user)
        await message.answer(texts.START_USER, reply_markup=buttons.MAIN_MENU)
    else:
        await message.answer(texts.START_USER, reply_markup=buttons.MAIN_MENU)
        
    await state.finish()
        
    
    
    
    
