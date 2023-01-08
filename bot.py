from pyrogram import Client
import os
from config import BOT_TOKEN, API_ID, API_HASH




    app = Client(
        "music_dl",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=300,
    )


app.run()
