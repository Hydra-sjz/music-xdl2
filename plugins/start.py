from pyrogram import Client, filters





@Client.on_message(filters.private & filters.command("start"))
async def start_command(_, message):
    await message.reply_text(f"Hi {message.from_user.mention}\n\nIm am music download bot for @songdownload_group group ‼️\nyou can download songs from there, just type /s or /song then write your song name.\ne.g: `/s alone`\n\nhttps://t.me/songdownload_group")
