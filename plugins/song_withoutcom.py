from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from database.decorators import humanbytes
#from database.filters import command, other_filters

from config import LOG_GROUP

 

ydl_opts = {
    'format': 'bestaudio',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True, 
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.group & filters.text)
def song(_, message):
    query=message.text
    print(query)
    #query = " ".join(message.command[1:])
    m = message.reply("ð <code>Searching your song</code>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"]
        views = results[0]["views"]
        performer = f"[á´á´sÉªá´ É¢á´Êá´xÊ]"
        channel = results[0]["channel"]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        if time_to_seconds(duration) >= 900:  # duration limit
            m.reply_photo(photo="https://telegra.ph/file/2d165d91b82dcab56d058.jpg", caption=f"â**DURATION LIMIT EXCEEDE:**â\n\nð **Allowed Duration:** 10 minute(s)\nð **Received Duration:** <code>{duration}</code>\nâ <b>Received video URL</b>: [click here]({link})\n\nSend songs less than 10 minutes")
            return

    except Exception as e:
        m.edit(f"Nothing Found {message.from_user.first_name} :(\n\nPlease check your using correct format Or your spelling are correct and try again.")
        print(str(e))
        return
    m.edit("ð½ <code>Downloading...</code>",
      reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Downloading...", callback_data="feed")
          ]]
          )
      )

    PForCopy = message.reply_photo(photo=f"{link}.jpg", caption=f"ð§<b>Title:</b> <code>{title}</code>\n<b>â±ï¸Duration:</b> <code>{duration}</code>\n<b>ðViews:</b> <code>{views}</code>\nð¤<b>Artist:</b> <code>{channel}</code>\nð<b>link:</b> [Click here]({link})\n\nð <b>By:</b> [ð á´sÉªá´âDÊ](t.me/Musicx_dlbot)")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"<code>{title}</code> | <b>{channel}</b>"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("ð¼ <code>Uploading to Telegram...</code>\n<i>(this may take a while.)</i>",
          reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Uploading...", callback_data="feed")
          ]]
          )
      )
        AForCopy = message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            performer=performer,
            title=title,
            duration=dur,
        )
        message.reply_sticker(sticker="CAACAgIAAxkBAAIS0WPb-Iq4TM7Bs67zYGG3JELnk1rsAAIoIAACJaYJS-FqCk576-FVHgQ",   
          reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Done â", url="t.me/Musicx_dlbot")
          ]]
          )
      )
        if LOG_GROUP:
            PForCopy.copy(LOG_GROUP)
            AForCopy.copy(LOG_GROUP)
            
        m.delete()
    except Exception as e:
        m.edit("#ERROR")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


