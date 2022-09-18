import asyncio
from pyrogram import Client

api_id = 1234567  # Sensitive data! Find your Telegram App api_id (at https://my.telegram.org/apps ) & paste it instead of 1234567
api_hash = "..."  # Sensitive data! Find your Telegram App api_hash here: https://my.telegram.org/apps

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "(Rumi) As you start to walk out on the way, the way appears")

asyncio.run(main())
