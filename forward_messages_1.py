# forward incomming messages to myself (to 'Saved messages' chat)
from pyrogram import Client

app = Client('my_account')


@app.on_message()
async def my_handler(client, message): # my_handler function accepts two arguments (client, message), will be executed every time a new message arrives
    await message.forward('me')


app.run()   # run() method without any argument: to automatically start(), keep the Client online so that it can listen for updates and stop() by CTRL+C

# Check https://docs.pyrogram.org/start/updates
