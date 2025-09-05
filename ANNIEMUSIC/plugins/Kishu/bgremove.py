import os
import aiohttp
import aiofiles
from pyrogram import filters
from ANNIEMUSIC import app

API_KEY = "23nfCEipDijgVv6SH14oktJe"

def generate_unique_filename(base_name: str) -> str:
    if os.path.exists(base_name):
        count = 1
        name, ext = os.path.splitext(base_name)
        while True:
            new_name = f"{name}_{count}{ext}"
            if not os.path.exists(new_name):
                return new_name
            count += 1
    return base_name

async def remove_background(image_path: str) -> tuple:
    headers = {"X-API-Key": API_KEY}
    async with aiohttp.ClientSession() as session:
        try:
            with open(image_path, "rb") as img:
                data = {"image_file": img.read()}
            async with session.post(
                "https://api.remove.bg/v1.0/removebg", headers=headers, data=data
            ) as response:

                if "image" not in response.headers.get("content-type", ""):
                    return False, await response.json()

                output_filename = generate_unique_filename("marin.png")
                async with aiofiles.open(output_filename, "wb") as out_file:
                    await out_file.write(await response.read())
                return True, output_filename

        except Exception as e:
            return False, {"title": "Unknown Error", "errors": [{"detail": str(e)}]}

@app.on_message(filters.command("rmbg"))
async def remove_bg_command(client, message):
    status = await message.reply("🖌️ Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ...")
    replied = message.reply_to_message

    if not replied or not replied.photo:
        return await status.edit("Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛs ʙᴀᴄᴋɢʀᴏᴜɴᴅ.")

    try:
        downloaded_photo = await client.download_media(replied)
        success, result = await remove_background(downloaded_photo)
        os.remove(downloaded_photo)

        if not success:
            error = result["errors"][0]
            return await status.edit(f"⚠️ ERROR: {result['title']}\n{error.get('detail', '')}")

        await message.reply_photo(photo=result, caption="✅ Hᴇʀᴇ's ʏᴏᴜʀ ɪᴍᴀɢᴇ ᴡɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ.")
        await message.reply_document(document=result)
        os.remove(result)
        await status.delete()

    except Exception as e:
        await status.edit(f"❌ Fᴀɪʟᴇᴅ ᴛᴏ ᴘʀᴏᴄᴇss ᴛʜᴇ ɪᴍᴀɢᴇ.\nError: {e}")
