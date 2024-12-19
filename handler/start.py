# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from services.services import createUser, getUser
from handler.channel.subscription import check_subscriptions



@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    
    get_user = getUser(user_id)
    user = {'user_id': user_id}
    
    not_exists = await check_subscriptions(bot, user_id)
    
    if not not_exists:
        if not get_user:
            createUser(user)
            await message.answer(texts.START_USER, reply_markup=buttons.MAIN_MENU)
        else:
            await message.answer(texts.START_USER, reply_markup=buttons.MAIN_MENU)
    else:
        keyboard = buttons.get_subscription_buttons(not_exists)
        await message.answer(texts.CHANNEL_REQUEST, reply_markup=keyboard)
        
    await state.finish()
        
    
    
    
    
