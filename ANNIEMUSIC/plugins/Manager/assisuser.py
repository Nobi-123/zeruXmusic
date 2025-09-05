import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
    ChannelPrivate,
    FloodWait,
    PeerIdInvalid,
)

from ANNIEMUSIC import app
from ANNIEMUSIC.utils.admin_filters import dev_filter, admin_filter, sudo_filter
from ANNIEMUSIC.utils.database import get_assistant


async def join_userbot(app, chat_id, chat_username=None):
    userbot = await get_assistant(chat_id)

    try:
        member = await app.get_chat_member(chat_id, userbot.id)
        if member.status == ChatMemberStatus.BANNED:
            await app.unban_chat_member(chat_id, userbot.id)
        elif member.status != ChatMemberStatus.LEFT:
            return "**🔥 Assɪsᴛᴀɴᴛ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.**"
    except PeerIdInvalid:
        return "**❌ Iɴᴠᴀʟɪᴅ ᴄʜᴀᴛ ID.**"
    except Exception:
        pass

    try:
        if chat_username:
            await userbot.join_chat(chat_username)
        else:
            invite_link = await app.create_chat_invite_link(chat_id)
            await userbot.join_chat(invite_link.invite_link)
        return "**❄️ Assɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.**"
    except UserAlreadyParticipant:
        return "**⚡ Assɪsᴛᴀɴᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛ.**"
    except Exception:
        try:
            if chat_username:
                await userbot.join_chat(chat_username)
            else:
                invite_link = await app.create_chat_invite_link(chat_id)
                await userbot.join_chat(invite_link.invite_link)
            return "**Assɪsᴛᴀɴᴛ sᴇɴᴛ ᴀ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ.🥀**"
        except AttributeError:
            return "**😓 Yᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴠᴇʀsɪᴏɴ ᴅᴏᴇsɴ'ᴛ sᴜᴘᴘᴏʀᴛ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛs.**"
        except Exception as e:
            return f"**❌ Fᴀɪʟᴇᴅ ᴛᴏ ᴀᴅᴅ ᴀssɪsᴛᴀɴᴛ: {str(e)}**"


@app.on_chat_join_request()
async def approve_join_request(client, chat_join_request: ChatJoinRequest):
    userbot = await get_assistant(chat_join_request.chat.id)
    if chat_join_request.from_user.id == userbot.id:
        await client.approve_chat_join_request(chat_join_request.chat.id, userbot.id)
        await client.send_message(
            chat_join_request.chat.id,
            "**⚡Assɪsᴛᴀɴᴛ ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ᴀɴᴅ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ.**",
        )


@app.on_message(
    filters.command(["userbotjoin", "assistantjoin"], prefixes=[".", "/"])
    & (filters.group | filters.private)
    & admin_filter
    & sudo_filter
)
async def join_group(app, message):
    chat_id = message.chat.id
    status_message = await message.reply("**⏳ Pʟᴇᴀsᴇ ᴡᴀɪᴛ, ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ...**")

    try:
        me = await app.get_me()
        chat_member = await app.get_chat_member(chat_id, me.id)
        if chat_member.status != ChatMemberStatus.ADMINISTRATOR:
            return await status_message.edit("**❌ I need to be admin to invite the assistant.**")
    except ChatAdminRequired:
        return await status_message.edit("**❌ I don't have permission to check admin status in this chat.**")
    except Exception as e:
        return await status_message.edit(f"**❌ Failed to verify permissions:** `{str(e)}`")

    chat_username = message.chat.username or None
    response = await join_userbot(app, chat_id, chat_username)
    await status_message.edit_text(response)


@app.on_message(
    filters.command("userbotleave", prefixes=[".", "/"])
    & filters.group
    & admin_filter
    & sudo_filter
)
async def leave_one(app, message):
    chat_id = message.chat.id
    try:
        userbot = await get_assistant(chat_id)
        member = await userbot.get_chat_member(chat_id, userbot.id)
        if member.status in [ChatMemberStatus.LEFT, ChatMemberStatus.BANNED]:
            return await message.reply("**Assɪsᴛᴀɴᴛ ɪs ɴᴏᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ. 😢.**")

        await userbot.leave_chat(chat_id)
        await app.send_message(chat_id, "**Assɪsᴛᴀɴᴛ ʜᴀs ʟᴇғᴛ ᴛʜɪs ᴄʜᴀᴛ. 🥀**")
    except ChannelPrivate:
        await message.reply("**❌ Error: This chat is not accessible or has been deleted.**")
    except UserNotParticipant:
        await message.reply("**Assɪsᴛᴀɴᴛ ɪs ɴᴏᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ. 😢.**")
    except Exception as e:
        await message.reply(f"**❌ Fᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀssɪsᴛᴀɴᴛ:** `{str(e)}`")


@app.on_message(filters.command("leaveall", prefixes=["."]) & dev_filter)
async def leave_all(app, message):
    left = 0
    failed = 0
    status_message = await message.reply("❄️**Assɪsᴛᴀɴᴛ ɪs ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs...**")

    try:
        userbot = await get_assistant(message.chat.id)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002681848382:
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
            except Exception:
                failed += 1

            await status_message.edit_text(
                f"**Leaving chats...**\n✅ Left: `{left}`\n❌ Failed: `{failed}`"
            )
            await asyncio.sleep(1)
    except FloodWait as e:
        await asyncio.sleep(e.value)
    finally:
        await app.send_message(
            message.chat.id,
            f"**✅ Left from:** `{left}` chats.\n**❌ Failed in:** `{failed}` chats.",
        )
