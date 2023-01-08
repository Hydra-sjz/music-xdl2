from pyrogram import Client
import os
from config import BOT_TOKEN, API_ID, API_HASH

from main.webcode import bot_run
from os import environ
from aiohttp import web as webserver

PORT_CODE = environ.get("PORT", "8080")



    app = Client(
        "music_dl",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=300,
    )

    async def start(self):
        await super().start()
        print("🎉🎉Bot Started 🎉🎉 Enjoy 🤯🥳")

        client = webserver.AppRunner(await bot_run())
        await client.setup()
        bind_address = "0.0.0.0"
        await webserver.TCPSite(client, bind_address, PORT_CODE).start()

app.run()
