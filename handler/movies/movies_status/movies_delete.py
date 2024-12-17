# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp

# add import
from asyncio import create_task




async def callback_delete_task(call: types.CallbackQuery, state: FSMContext):

    """
    Tashlab berilgan kinoni pasidagi status (tashlab berilgan kinoni ochirish uchun)
    """

    try:
        await call.message.delete()
    except Exception as e:
        await call.answer(f"Xabarni o'chirishda xatolik yuz berdi")



@dp.callback_query_handler(lambda call: call.data == 'delete', state="*")
async def callback_delete(call: types.CallbackQuery, state: FSMContext):
  create_task(callback_delete_task(call, state))
