import asyncio
from pyrogram import Client

try:
    # ✅ New API in pytgcalls==3.0.0.dev24
    from pytgcalls import GroupCallFactory
except ImportError:
    raise ImportError("Please install pytgcalls==3.0.0.dev24 or compatible version.")

try:
    # ✅ NoActiveGroupCall is removed, use GroupCallNotFoundError instead
    from pytgcalls.exceptions import GroupCallNotFoundError as NoActiveGroupCall
except ImportError:
    class NoActiveGroupCall(Exception):
        pass


import config
from ANNIEMUSIC import userbot


class Call:
    def __init__(self):
        # ✅ Replace PyTgCalls with GroupCallFactory().get_group_call()
        self.one = GroupCallFactory(userbot).get_group_call()

    async def start(self):
        await self.one.start()

    async def stream_call(self, link: str):
        await self.one.join_group_call(
            config.LOG_GROUP_ID,
            self.one.input_filename(link),
        )

    async def decorators(self):
        # Keep this as it was in your original file
        pass


# ✅ Export instance
JARVIS = Call()
