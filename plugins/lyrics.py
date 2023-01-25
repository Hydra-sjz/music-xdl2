import os
import re

import lyricsgenius
from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(filters.command(["lyrics", "lyric"]))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n/lyrics [ Music Name]")
    m = await message.reply_text("Searching Lyrics")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not found :p")
    xxx = f"""
**Lyrics Search Powered By Music X dl**

**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}

**__Lyrics:__**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
