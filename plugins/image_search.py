from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from requests import get

from VIPMUSIC import app


@app.on_message(
    filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def pinterest(_, message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

    media_group = []
    count = 0

    msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
    for url in images["images"][:6]:

        media_group.append(InputMediaPhoto(media=url))
        count += 1
        await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

    try:

        await app.send_media_group(
            chat_id=chat_id, media=media_group, reply_to_message_id=message.id
        )
        return await msg.delete()

    except Exception as e:
        await msg.delete()
        return await message.reply(f"ᴇʀʀᴏʀ : {e}")


__MODULE__ = "ɪᴍᴀɢᴇ ꜱᴇᴀʀᴄʜ"
__HELP__ = """
**ᴘɪɴᴛᴇʀᴇsᴛ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ**

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀʟʟᴏᴡs ᴜsᴇʀs ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ɪᴍᴀɢᴇs ᴏɴ ᴘɪɴᴛᴇʀᴇsᴛ ᴀɴᴅ sᴇɴᴅs ᴀ ᴄᴏᴇᴄᴛɪᴏɴ ᴏғ ᴜᴘ ᴛᴏ 6 ɪᴍᴀɢᴇs.

ғᴇᴀᴛᴜʀᴇs:
- Rᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ ᴏ̨ᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ɪᴍᴀɢᴇs ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ ᴏ̨ᴜᴇʀʏ ᴏɴ ᴘɪɴᴛᴇʀᴇsᴛ.
- sᴇɴᴅs ᴜᴘ ᴛᴏ 6 ɪᴍᴀɢᴇs ғᴏᴜɴᴅ ᴏɴ ᴘɪɴᴛᴇʀᴇsᴛ ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ᴏ̨ᴜᴇʀʏ.

ᴄᴏᴍᴍᴀɴᴅs:
- /image <ᴏ̨ᴜᴇʀʏ>: sᴇᴀʀᴄʜ ғᴏʀ ɪᴍᴀɢᴇs ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴏ̨ᴜᴇʀʏ ᴏɴ ᴘɪɴᴛᴇʀᴇsᴛ.

ᴇxᴀᴍᴘʟᴇ:
- /ɪᴍᴀɢᴇ <ᴏ̨ᴜᴇʀʏ>: sᴇᴀʀᴄʜᴇs ғᴏʀ ɪᴍᴀɢᴇs ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴏ̨ᴜᴇʀʏ ᴏɴ ᴘɪɴᴛᴇʀᴇsᴛ ᴀɴᴅ sᴇɴᴅs ᴜᴘ ᴛᴏ 6 ɪᴍᴀɢᴇs.

ɴᴏᴛᴇ: ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇs ᴀɴ ᴇxᴛᴇʀɴᴀʟ ᴘɪɴᴛᴇʀᴇsᴛ API ᴛᴏ ғᴇᴛᴄʜ ɪᴍᴀɢᴇs.
"""
