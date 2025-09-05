import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from ntgcalls import TelegramServerError
from pyrogram import Client
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import NoActiveGroupCall
from pytgcalls.types import AudioQuality, ChatUpdate, MediaStream, StreamEnded, Update, VideoQuality

import config
from strings import get_string
from ANNIEMUSIC import LOGGER, YouTube, app
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
        self.userbot1 = Client("AnnieXAssis1", config.API_ID, config.API_HASH, session_string=config.STRING1) if config.STRING1 else None
        self.one = PyTgCalls(self.userbot1) if self.userbot1 else None

        self.userbot2 = Client("AnnieXAssis2", config.API_ID, config.API_HASH, session_string=config.STRING2) if config.STRING2 else None
        self.two = PyTgCalls(self.userbot2) if self.userbot2 else None

        self.userbot3 = Client("AnnieXAssis3", config.API_ID, config.API_HASH, session_string=config.STRING3) if config.STRING3 else None
        self.three = PyTgCalls(self.userbot3) if self.userbot3 else None

        self.userbot4 = Client("AnnieXAssis4", config.API_ID, config.API_HASH, session_string=config.STRING4) if config.STRING4 else None
        self.four = PyTgCalls(self.userbot4) if self.userbot4 else None

        self.userbot5 = Client("AnnieXAssis5", config.API_ID, config.API_HASH, session_string=config.STRING5) if config.STRING5 else None
        self.five = PyTgCalls(self.userbot5) if self.userbot5 else None

        self.active_calls: set[int] = set()

    async def auto_start(self):
        LOGGER(__name__).info("Auto-starting all Pyrogram Clients...")
        for client in [self.userbot1, self.userbot2, self.userbot3, self.userbot4, self.userbot5]:
            if client and not client.is_connected:
                await client.start()
        for call in [self.one, self.two, self.three, self.four, self.five]:
            if call:
                await call.start()

    # ... (all other methods remain the same)

JARVIS = Call()
