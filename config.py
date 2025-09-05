import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ───── Basic Bot Configuration ───── #
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 7694170809))
OWNER_USERNAME = getenv("OWNER_USERNAME", "x9Ahad")
BOT_USERNAME = getenv("BOT_USERNAME", "PreetixMusic_bot")
BOT_NAME = getenv("BOT_NAME", "- `𝐂α᱂ᴅɪᴏ ꭗ‌ 𝐌ᴜѕɪᴄ")
ASSUSERNAME = getenv("ASSUSERNAME", "PreetixAssistant")
EVALOP = list(map(int, getenv("EVALOP", "6797202080").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1002681848382))

# ───── Limits and Durations ───── #
RESTART_INTERVAL = int(getenv("RESTART_INTERVAL", 86400))  # default 24 hours
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ───── Custom API Configs ───── #
API_URL = getenv("API_URL") #optional
API_KEY = getenv("API_KEY") #optional
COOKIE_URL = getenv("COOKIE_URL") #necessary
DEEP_API = getenv("DEEP_API") #optional

# ───── Heroku Configuration ───── #
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ───── Git & Updates ───── #
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Nobi-123/ZERATHOSxMUSIC")
UPSTREAM_BRANCH = "main"
GIT_TOKEN = getenv("GIT_TOKEN", "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")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botXjarvis")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/jarvisXsupport")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG =True

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings ───── #
STRING1 = getenv("STRING_SESSION"," AgCOaU4AMhs2zXt5ZMPUxy6CCi5UXkrxiw9K6waJak3cY2rNexhzgop077ISfte_6tFc9PS4yAB61_hL8-MEij2j-y4O2liZikwKuFWKNhWIyOPHuV4WV9yEEUbZvTdp5Fi0fTWPNxe7Ks_bJjPPyI4khC9HNWwj6WGxeUbkBOcpVROP9kqV7JXLa9DUdBeKZ_QivQXeIHgdBNJJRCWa36kn5w46Zw85KHjYyc-UxR6KARoF1ErX076O27S_MJE4S7FgpRnJme7gAEATacznecxgUQ4KV-Aa_sX_341fnSXpaV4kpmjAYl6NEplLYmCHBpmq2MDDoAArtfHvu6_tFHuWX1HFXAAAAAHR4jcZAA")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ───── Server Settings ───── #
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# ───── Bot Media Assets ───── #

START_VIDS = [
    "ANNIEMUSIC/assets/annie/uff.mp4",
    "ANNIEMUSIC/assets/annie/yeah.mp4",
    "ANNIEMUSIC/assets/annie/oh.mp4",
    "ANNIEMUSIC/assets/annie/nah.mp4"
    "ANNIEMUSIC/assets/annie/hein.mp4"
    "ANNIEMUSIC/assets/annie/hein.mp4"
]

STICKERS = [
    "CAACAgUAAxkBAAJ9b2i3sIW0gLK-9ibLUB40kt20geGxAAKXFgACAiuIV3_FTwqaZghPHgQ",
    "CAACAgUAAxkBAAJ9cGi3sId1J4t8J5QMnlCfOC4WJjg2AAJ_EwAC1bGJV_V1r5ipRn-MHgQ",
    "CAACAgUAAxkBAAJ9cWi3sIpJXocM64UNYVq9J5WkNYeTAAKpEgACT_2JVy9ts-zlPvBfHgQ",
    "CAACAgUAAxkBAAJ9c2i3sJVnR-yJpDI6CxrBKha0E7aoAAKrEgACHHqJV84cBIZIiBVTHgQ",
    "CAACAgUAAxkBAAJ9cWi3sIpJXocM64UNYVq9J5WkNYeTAAKpEgACT_2JVy9ts-zlPvBfHgQ"
]
HELP_IMG_URL = [
    "ANNIEMUSIC/assets/annie/aaa.jpeg",
    "ANNIEMUSIC/assets/annie/bo.jpeg",
    "ANNIEMUSIC/assets/annie/hurr.jpeg",
    "ANNIEMUSIC/assets/annie/hehe.jpeg",
    "ANNIEMUSIC/assets/annie/ipl.jpeg",
    "ANNIEMUSIC/assets/annie/ji.jpeg",
    "ANNIEMUSIC/assets/annie/kit.jpeg",
    "ANNIEMUSIC/assets/annie/li.jpeg",
    "ANNIEMUSIC/assets/annie/marin.jpeg",
    "ANNIEMUSIC/assets/annie/soo.jpeg"
    
]

PING_VID_URL = "ANNIEMUSIC/assets/annie/oh.mp4"
PLAYLIST_IMG_URL = "ANNIEMUSIC/assets/annie/kit.jpeg"
STATS_VID_URL = "ANNIEMUSIC/assets/annie/li.jpeg"
TELEGRAM_AUDIO_URL = "ANNIEMUSIC/assets/annie/marin.jpeg"
TELEGRAM_VIDEO_URL = "ANNIEMUSIC/assets/annie/soo.jpeg"
STREAM_IMG_URL = "ANNIEMUSIC/assets/annie/hehe.jpeg"
SOUNCLOUD_IMG_URL = "ANNIEMUSIC/assets/annie/aaa.jpeg"
YOUTUBE_IMG_URL = "ANNIEMUSIC/assets/annie/ipl.jpeg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┗━━━━━━━━━━━━━━━━━⧫\n\n",
    "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┗━━━━━━━━━━━━━━━━━⧫\n\n",
]

# ───── Runtime Structures ───── #
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ───── URL Validation ───── #
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
