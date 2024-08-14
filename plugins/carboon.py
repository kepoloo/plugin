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
**ᴄᴀʀʙᴏɴ ᴄᴏᴍᴍᴀɴᴅ**

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀʟᴏᴡs ᴜsᴇʀs ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ. ᴄᴀʀʙᴏɴ ɪs ᴀ ᴛᴏᴏ ғᴏʀ ᴄʀᴇᴀᴛɪɴɢ ʙᴇᴀᴜᴛɪғᴜʟ ɪᴍᴀɢᴇs ᴏғ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.

ғᴇᴀᴛᴜʀᴇs:
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴇɴᴛ.
- sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴘᴀɪɴ ᴛᴇxᴛ ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴᴇᴅ ᴍᴇssᴀɢᴇs.
- ᴅɪsᴘʟᴀʏs ᴀ ᴘʀᴏᴄᴇssɪɴɢ ᴍᴇssᴀɢᴇ ᴡʜɪᴇ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴛʜᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ.
- ᴜᴘʟᴏᴀᴅs ᴛʜᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ᴍᴇssᴀɢᴇ.

ᴄᴏᴍᴍᴀɴᴅs:
- /carbon: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴇɴᴛ.

ɴᴏᴛᴇ: ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ sᴜᴄᴄᴇssғᴜʏ.
"""
