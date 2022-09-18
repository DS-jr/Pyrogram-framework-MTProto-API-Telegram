from pyrogram import Client
from pyrogram.handlers import MessageHandler

api_id = 1234567  # Sensitive data! Find your Telegram App api_id here: https://my.telegram.org/apps
api_hash = "..."  # Sensitive data! Find your Telegram App api_hash here: https://my.telegram.org/apps

# @app.on_message()   # on_message() is a decorator
async def my_function(client, message):
    await message.forward("me")


app1 = Client("my_account", api_id=api_id, api_hash=api_hash)


my_handler = MessageHandler(my_function)
app1.add_handler(my_handler)  # add_handler() method takes any handler instance that wraps around your defined callback function and registers it in your Client.


app1.run()
