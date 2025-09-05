from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from config import *
from ANNIEMUSIC import app
from ANNIEMUSIC.core.call import JARVIS
from ANNIEMUSIC.utils import bot_sys_stats
from ANNIEMUSIC.utils.decorators.language import language
from ANNIEMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_VID_URL


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    # ✅ Flexible handling for image/video/text
    if PING_VID_URL and PING_VID_URL.lower().endswith((".mp4", ".mkv")):
        response = await message.reply_video(
            video=PING_VID_URL,
            caption=_["ping_1"].format(app.mention),
        )
        edit_func = response.edit_caption
    elif PING_VID_URL and PING_VID_URL.lower().endswith((".png", ".jpg", ".jpeg")):
        response = await message.reply_photo(
            photo=PING_VID_URL,
            caption=_["ping_1"].format(app.mention),
        )
        edit_func = response.edit_caption
    else:
        response = await message.reply_text(
            text=_["ping_1"].format(app.mention),
        )
        edit_func = response.edit_text

    pytgping = await JARVIS.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await edit_func(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
