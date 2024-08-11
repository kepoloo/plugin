import os
import shutil

from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


@app.on_message(filters.command("clean") & SUDOERS)
async def clean(_, message):
    A = await message.reply_text("ᴄʟᴇᴀɴɪɴɢ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs...")
    dir = "downloads"
    dir1 = "cache"
    shutil.rmtree(dir)
    shutil.rmtree(dir1)
    os.mkdir(dir)
    os.mkdir(dir1)
    await A.edit("ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴀʀᴇ ᴄʟᴇᴀɴᴇᴅ")


__MODULE__ = "ᴄʟᴇᴀɴ"
__HELP__ = """
## Cʟᴇᴀɴ Cᴏᴍᴍᴀɴᴅ

### Cᴏᴍᴍᴀɴᴅ: /clean
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Cʟᴇᴀɴs ᴜᴘ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴛᴏ ғʀᴇᴇ ᴜᴘ sᴘᴀᴄᴇ.

**Usᴀɢᴇ:**
/clean

**Dᴇᴛᴀʟɪs:**
- Dᴇʟᴇᴛᴇs ᴛʜᴇ 'ᴅᴏᴡɴʟᴏᴀᴅs' ᴀɴᴅ 'ᴄᴀᴄʜᴇ' ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴀɴᴅ ʀᴇᴄʀᴇᴀᴛᴇs ᴛʜᴇᴍ ᴛᴏ ᴇɴsᴜʀᴇ ᴛᴇᴍᴘᴏʀᴀʀʏ ғɪᴇs ᴀʀᴇ ʀᴇᴍᴏᴠᴇᴅ.
- Oɴʟʏ ᴀᴄᴄᴇssɪʙᴇ ᴛᴏ ᴜsᴇʀs ɪɴ ᴛʜᴇ SUDOERS ɪsᴛ.
"""
