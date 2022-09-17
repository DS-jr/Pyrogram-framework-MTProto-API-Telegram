from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.text & filters.private)  # reply to private text messages only
async def echo(client, message):
    await message.reply(message.text)


app.run()
