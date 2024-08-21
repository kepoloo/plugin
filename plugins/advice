from pyrogram import filters


from VIPMUSIC import api, app


async def get_advice():
    b = await api.advice()
    c = b["advice"]
    return c


@app.on_message(filters.command("advice"))
async def clean(_, message):
    A = await message.reply_text("...")
    B = await get_advice()
    await A.edit(B)


__MODULE__ = "ᴀᴅᴠɪᴄᴇ"
__HELP__ = """
ᴀᴅᴠɪᴄᴇ ᴄᴏᴍᴍᴀɴᴅ

ᴄᴏᴍᴍᴀɴᴅ: /ᴀᴅᴠɪᴄᴇ
**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:**
ғᴇᴛᴄʜᴇs ᴀ ʀᴀɴᴅᴏᴍ ᴘɪᴇᴄᴇ ᴏғ ᴀᴅᴠɪᴄᴇ ғʀᴏᴍ ᴀɴ API ᴀɴᴅ ᴅɪsᴘʟᴀʏs ɪᴛ.
**ᴜsᴀɢᴇ:**
/advice

**ᴅᴇᴛᴀɪʟs:**
- sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴘɪᴇᴄᴇ ᴏғ ᴀᴅᴠɪᴄᴇ ᴀs ᴀ ᴍᴇssᴀɢᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

**ᴇxᴀᴍᴘʟᴇs:**
- /ᴀᴅᴠɪᴄᴇ: ʀᴇᴛʀɪᴇᴠᴇs ᴀɴᴅ ᴅɪsᴘʟᴀʏs ᴀᴅᴠɪᴄᴇ.

**ɴᴏᴛᴇs:**
- Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ᴜsᴇʀ ᴛᴏ ɢᴇᴛ ᴀ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ.
"""
