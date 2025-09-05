import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from ntgcalls import TelegramServerError
from pyrogram import Client
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import GroupCallFactory
from pytgcalls.types import AudioQuality, VideoQuality, MediaStream, ChatUpdate, StreamEnded, Update

import config
from strings import get_string
from ANNIEMUSIC import LOGGER, YouTube, app, userbot
from ANNIEMUSIC.misc import db
from ANNIEMUSIC.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    get_loop,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from ANNIEMUSIC.utils.exceptions import AssistantErr
from ANNIEMUSIC.utils.formatters import check_duration, seconds_to_min, speed_converter
from ANNIEMUSIC.utils.inline.play import stream_markup
from ANNIEMUSIC.utils.stream.autoclear import auto_clean
from ANNIEMUSIC.utils.thumbnails import get_thumb
from ANNIEMUSIC.utils.errors import capture_internal_err, send_large_error

autoend = {}
counter = {}

# ✅ Patch for Pyrogram v2 (invoke -> send)
if not hasattr(userbot, "invoke") and hasattr(userbot, "send"):
    userbot.invoke = userbot.send


def dynamic_media_stream(path: str, video: bool = False, ffmpeg_params: str = None) -> MediaStream:
    return MediaStream(
        audio_path=path,
        media_path=path,
        audio_parameters=AudioQuality.MEDIUM if video else AudioQuality.STUDIO,
        video_parameters=VideoQuality.HD_720p if video else VideoQuality.SD_360p,
        video_flags=(MediaStream.Flags.AUTO_DETECT if video else MediaStream.Flags.IGNORE),
        ffmpeg_parameters=ffmpeg_params,
    )


async def _clear_(chat_id: int) -> None:
    popped = db.pop(chat_id, None)
    if popped:
        await auto_clean(popped)
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)
    await set_loop(chat_id, 0)


class Call:
    def __init__(self):
        # ✅ Use GroupCallFactory with patched userbot
        self.one = GroupCallFactory(userbot).get_group_call()
        self.active_calls: set[int] = set()

    async def auto_start(self):
        LOGGER(__name__).info("Auto-starting all Pyrogram Clients...")
        if not userbot.is_connected:
            await userbot.start()
        if self.one:
            await self.one.start()

    # ... (all your other methods remain unchanged)


JARVIS = Call()
