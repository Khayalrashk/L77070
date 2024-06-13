from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني إلى مجموعتك او قناتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="𝐃𝐞𝐯", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=config.CHANNEL_NAME, url=config.CHANNEL_LINK)
        ],
        [InlineKeyboardButton(text="○ 𝐌𝐲 𝐖𝐨𝐫𝐥𝐝 ○", url=f"https://t.me/KHAYAL70"),
],

    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني إلى مجموعتك او قناتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="𝐃𝐞𝐯", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=config.CHANNEL_NAME, url=config.CHANNEL_LINK)
        ],
        [InlineKeyboardButton(text="○ 𝐌𝐲 𝐖𝐨𝐫𝐥𝐝 ○", url=f"https://t.me/KHAYAL70"),
 ],
    ]
    return buttons
