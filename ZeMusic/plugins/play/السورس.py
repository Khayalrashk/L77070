import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2f199ef466e7950dd5e79.jpg",
        caption = f"""<b>⌯ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 . .<b>\n<a href="https://t.me/yut70">⌯ 𝐬𝐨𝐮𝐫𝐜𝐞 𝐬𝐢𝐦𝐚 ⛧</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𝐬𝐨𝐮𝐫𝐜𝐞 𝐬𝐢𝐦𝐚 ›", url=f"https://t.me/yut70"),         
                ],

            ]

        ),

    )
