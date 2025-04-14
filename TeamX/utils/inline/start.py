from pyrogram.types import InlineKeyboardButton

import config
from TeamX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
         InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
         InlineKeyboardButton("[❄️] 𝐁σт 𝐈иғσ [❄️]", callback_data="bot_info_data"),
        ],
        # [
        #     InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        #     InlineKeyboardButton(text=_["S_B_7"], user_id=config.CO_OWNER_ID),
        # ],
    ]
    return buttons


