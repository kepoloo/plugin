from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app


@app.on_message(filters.command(["dice", "ludo"]))
async def dice(c, m: Message):
    dicen = await c.send_dice(m.chat.id, reply_to_message_id=m.id)
    await dicen.reply_text("results is {0}".format(dicen.dice.value))


__MODULE__ = "ꜰᴜɴ"
__HELP__ = """
ғᴜɴ ᴄᴏᴍᴍᴀɴᴅs ʜᴇʟᴘ

**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:**
ʀᴏsᴇ ᴀ ᴠɪʀᴛᴜᴀʟ ᴅɪᴄᴇ ᴏʀ ᴘᴀʏs ᴀ ɢᴀᴍᴇ ᴏғ Lᴜᴅᴏ.

**ᴜsᴀɢᴇ:**
/dice ᴏʀ /ludo

**ᴅᴇᴛᴀɪʟs:**
- ɪɴɪᴛɪᴀᴛᴇs ᴀ ᴅɪᴄᴇ ʀᴏ ᴏʀ ᴀ ɢᴀᴍᴇ ᴏғ ʟᴜᴅᴏ.
- Sᴇɴᴅs ᴛʜᴇ ʀᴇsᴜᴛ ᴏғ ᴛʜᴇ ᴅɪᴄᴇ ʀᴏ.
- Fᴏʀ Lᴜᴅᴏ, ᴛʜᴇ ɢᴀᴍᴇ ɪs ᴘᴀʏᴇᴅ ᴅɪʀᴇᴄᴛʏ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

"""
