from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot




@dp.message_handler(content_types=['video'])
async def file_id(message: Message, state: FSMContext):
    video = message.video.file_id
    await message.answer(video)
