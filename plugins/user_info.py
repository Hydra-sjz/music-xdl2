import os
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# private id===============
@Client.on_message(filters.command("id"))
async def id_(bot: Client, msg: Message):
	if not msg.chat.type == "private":
		main = f"**This {msg.chat.type} ɪᴅ is** `{msg.chat.id}`\n**User Id is:** `{msg.from_user.id}`"
		if msg.reply_to_message:
			if msg.reply_to_message.from_user:
				main = f"{msg.reply_to_message.from_user.first_name} your id is `{msg.reply_to_message.from_user.id}`\n\n**Message_id:**\nhttps://t.me/{msg.chat.username}/{msg.reply_to_message.message_id}"
				if msg.reply_to_message.sticker:
					main += f"\n\n**Your Requested Sticker ID is:**\n`{msg.reply_to_message.sticker.file_id}`"

		await msg.reply(main)
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Yᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ ɪs: `{msg.from_user.id}`", quote=True)
		if len(msg.command) == 2:
			try:
				uname = msg.command[1]
				if uname.startswith("@"):
					uname = uname[1:]
				try:
					user = await bot.get_users(uname)
					name = user.mention
					if len(user.first_name) <= 20:
						pass
					elif user.is_bot:
						name = "This Bot"
					else:
						name = "This User"
				except IndexError:
					user = await bot.get_chat(uname)
					name = '@'+user.username if user.username else user.title
				id = user.id
				await msg.reply(f"{name}'s ɪᴅ ɪs `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("Tʜɪs ᴜsᴇʀɴᴀᴍᴇ ɪs ɴᴏᴛ ᴏᴄᴄᴜᴘɪᴇᴅ ʙʏ ᴀɴʏᴏɴᴇ", quote=True)

# Sticker id-------
@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**ʜᴇʀᴇ ɪs ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ɪᴅ**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** ᴜɴɪǫᴜᴇ ɪᴅ ɪs ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("ɴɪᴄᴇ,ɪᴛs ɴᴏᴛ ᴀ sᴛɪᴄᴋᴇʀ")

# Dc finder
@Client.on_message(filters.private & filters.command(["dc"]))
async def dc(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

START_TEXT = "Yᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴄ ɪs : `{}`"
