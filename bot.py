from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN



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

    
        

bot = Bot()
bot.run()
