import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(
    command(["المبرمج","مبرمج","مبرمج السورس","مطور السورس","خيال"])
)
async def yas(client, message):
    usr = await client.get_chat("F_A_6")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"-› 𝙽𝙰𝙼𝙴 ¦ :{name}\n -› 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 ¦ :@{usr.username}\n -› 𝙸𝙳 ¦ :`{usr.id}`\n -› 𝙱𝙸𝙾 ¦ :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         name, url=f"https://t.me/{usrnam}"), 
                 ],[
                   InlineKeyboardButton(
                        "• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 ♩", url=f"https://t.me/SOURCELARIN"),
                ],

            ]

        ),

    )
