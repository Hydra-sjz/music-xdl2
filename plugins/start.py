from pyrogram import Client, filters
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton





@Client.on_message(filters.private & filters.command("start"))
async def start_command(_, message):
    await message.reply_photo(photo="https://telegra.ph/file/ceeca2da01f5d39550111.jpg", caption=f"»━━━━━━«[𝗠ᴜsɪᴄ✘Dʟ]»━━━━━━«\n\nHi there {message.from_user.mention} ♥️♣️\n\nMy Name is 🎶[𝗠ᴜsɪᴄ✘Dʟ](t.me/Musicx_dlbot) Bot,and I'm a simple and 🏖️Advanced Audio & Video downloader bot with higher quality 🎛️.\n\nHow it's work🤔\n <b>Audio 💽</b>\ntype /s or /song then write your song name.\ne.g: `/s alone`\n<b>Video 📹</b>\ntype /v or /video then write your song name.\ne.g: `/v hope`\nⓂ️©️ @songdownload_group\n\n»━━━━━━━━━━━━━━━━━━«")
                  Y
