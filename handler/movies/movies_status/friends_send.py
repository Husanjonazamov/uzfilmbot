# aiogram import
from aiogram.dispatcher import FSMContext
from aiogram import types

# kode import
from loader import dp

# add import
from asyncio import create_task



async def inline_query_handler_task(inline_query: types.InlineQuery):

    """
    Tashlab berilgan kinoni pasidagi status (Dostlarga yuborish uchun)
    """

    try:
        results = [
            types.InlineQueryResultArticle(
                id="1",
                title="Do'stlarga ulashish",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{inline_query.query}"
                ),
                description="Kino ulashish",
                thumb_url="https://example.com/thumb.jpg"  
            )
        ]
        await inline_query.answer(results)
    except Exception as e:
        await inline_query.answer(f"Xabarni ulashishda xatolik yuz berdi: {e}")


@dp.inline_handler()
async def inline_query_handler(inline_query: types.InlineQuery, state: FSMContext):
  create_task(inline_query_handler_task(inline_query, state))