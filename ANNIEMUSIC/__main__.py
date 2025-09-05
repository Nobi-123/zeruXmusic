import asyncio
import importlib

from pyrogram import idle

# ✅ Handle NoActiveGroupCall replacement (since it's removed in v3)
try:
    from pytgcalls.exceptions import GroupCallNotFoundError as NoActiveGroupCall
except ImportError:
    class NoActiveGroupCall(Exception):
        pass

import config
from ANNIEMUSIC import LOGGER, app, userbot
from ANNIEMUSIC.core.call import JARVIS
from ANNIEMUSIC.misc import sudo
from ANNIEMUSIC.plugins import ALL_MODULES
from ANNIEMUSIC.utils.database import get_banned_users, get_gbanned
from ANNIEMUSIC.utils.cookie_handler import fetch_and_store_cookies
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ sᴇssɪᴏɴ ɴᴏᴛ ғɪʟʟᴇᴅ, ᴘʟᴇᴀsᴇ ғɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ...")
        exit()

    # ✅ Try to fetch cookies at startup
    try:
        await fetch_and_store_cookies()
        LOGGER("ANNIEMUSIC").info("ʏᴏᴜᴛᴜʙᴇ ᴄᴏᴏᴋɪᴇs ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")
    except Exception as e:
        LOGGER("ANNIEMUSIC").warning(f"⚠️ Cookie error: {e}")

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ANNIEMUSIC.plugins" + all_module)

    LOGGER("ANNIEMUSIC.plugins").info("ᴍᴀʀɪɴ's modules loaded...")

    await userbot.start()
    await JARVIS.auto_start()

    # ✅ Fixed: use join_group_call instead of old stream_call
    try:
        if JARVIS.one:
            await JARVIS.one.join_group_call(
                config.LOGGER_ID,  # replace with your log group/channel ID
                JARVIS.dynamic_media_stream("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"),
            )
    except NoActiveGroupCall:
        LOGGER("ANNIEMUSIC").error(
            "ᴘʟᴇᴀsᴇ turn on the voice chat of your log group/channel.\n\nᴍᴀʀɪɴ ʙᴏᴛ stopped..."
        )
        exit()
    except Exception as e:
        LOGGER("ANNIEMUSIC").warning(f"⚠️ Group call join error: {e}")

    await JARVIS.decorators()
    LOGGER("ANNIEMUSIC").info("Annie Music Robot Started Successfully ✅")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ANNIEMUSIC").info("Stopping Annie Music Bot ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
