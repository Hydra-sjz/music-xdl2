from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, PORT

from aiohttp import web
from plugins import web_server


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="song_dl",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
    
        

bot = Bot()
bot.run()
