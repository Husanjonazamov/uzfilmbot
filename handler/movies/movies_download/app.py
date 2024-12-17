import os
from pyrogram import Client

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

app = Client("MoviesTvBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def start_client():
    if not app.is_connected:
        await app.start()

async def stop_client():
    if app.is_connected:
        await app.stop()
