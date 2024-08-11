from io import BytesIO

import aiohttp
from pyrogram import filters

from VIPMUSIC import app


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ.**")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ.**")
    text = await message.reply("Processing...")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()


__MODULE__ = "ᴄᴀʀʙᴏɴ"
__HELP__ = """
**Cᴀʀʙᴏɴ Cᴏᴍᴍᴀɴᴅ**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀʟᴏᴡs ᴜsᴇʀs ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ. Cᴀʀʙᴏɴ ɪs ᴀ ᴛᴏᴏ ғᴏʀ ᴄʀᴇᴀᴛɪɴɢ ʙᴇᴀᴜᴛɪғᴜʟ ɪᴍᴀɢᴇs ᴏғ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.

Fᴇᴀᴛᴜʀᴇs:
- Rᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴇɴᴛ.
- Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴘᴀɪɴ ᴛᴇxᴛ ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴᴇᴅ ᴍᴇssᴀɢᴇs.
- Dɪsᴘʟᴀʏs ᴀ ᴘʀᴏᴄᴇssɪɴɢ ᴍᴇssᴀɢᴇ ᴡʜɪᴇ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴛʜᴇ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ.
- Uᴘʟᴏᴀᴅs ᴛʜᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ᴍᴇssᴀɢᴇ.

Cᴏᴍᴍᴀɴᴅs:
- /carbon: Rᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴇɴᴛ.

Nᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ sᴜᴄᴄᴇssғᴜʏ.
"""
