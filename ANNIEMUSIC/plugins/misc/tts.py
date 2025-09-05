from __future__ import annotations

import asyncio
import os
from typing import Dict, Tuple

import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import Message

from ANNIEMUSIC import app

# ---------------------------------------------------------------------------
# Global constants
# ---------------------------------------------------------------------------
TMP_DIR = "/tmp"   # location for temporary audio / text files
_voice_sessions: Dict[Tuple[int, int], str] = {}

# ElevenLabs credentials
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "E7bpJOpaUwdzBn3Wd6Lr")

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def _cleanup(path: str) -> None:
    if os.path.exists(path):
        os.remove(path)


async def _synthesize(text: str, out_path: str) -> None:
    """Gᴇɴᴇʀᴀᴛᴇ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴜsɪɴɢ Mᴀʀɪɴ Tᴛs."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "accept": "audio/mpeg",
        "Content-Type": "application/json"
    }
    payload = {"text": text}

    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code != 200:
        raise Exception(f"MARIN TTS failed: {resp.text}")

    with open(out_path, "wb") as f:
        f.write(resp.content)

# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
@app.on_message(filters.command("tts"))
async def cmd_tts(client: Client, message: Message):
    """Direct `/tts <text>` ᴄᴏᴍᴍᴀɴᴅ ᴜsɪɴɢ Mᴀʀɪɴ ᴠᴏɪᴄᴇ."""
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n`/tts <text>`\nExample: `/tts Hello world!`",
            parse_mode=ParseMode.MARKDOWN,
        )

    text = message.text.split(" ", 1)[1]
    tmp = os.path.join(TMP_DIR, f"marin.mp3")

    try:
        await client.send_chat_action(message.chat.id, ChatAction.RECORD_AUDIO)
        await _synthesize(text, tmp)

        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_AUDIO)
        await client.send_audio(
            chat_id=message.chat.id,
            audio=tmp,
            caption=f"🗣️ Gᴇɴᴇʀᴀᴛᴇᴅ ᴡɪᴛʜ Mᴀʀɪɴ ᴠᴏɪᴄᴇ",
            reply_to_message_id=message.id,
            parse_mode=ParseMode.MARKDOWN,
        )
    except Exception as exc:
        print(f"[TTS ERROR] {exc}")
        await message.reply_text("⚠️ Failed to generate speech.")
    finally:
        _cleanup(tmp)
