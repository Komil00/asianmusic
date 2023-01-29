import asyncio
from pyrogram import Client

api_id = 29349324
api_hash = "d41f283e52b3cc850206f14bd467affe"
bot_token = "2083963103:AAGCaOvpcRhUThuZRcRvooP3VjLMknLSDBU"
app = Client("account", api_id, api_hash)

with app:
    for a in app.get_chat_photos("@Shakhob_tagaev"):
        print(a)
        d =  a.thumbs[0].file_id
        app.send_photo('@Shakhob_tagaev', photo=d)
