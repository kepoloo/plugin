from pyrogram import filters

from VIPMUSIC import app


@app.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"Error: {e}")
    else:
        message.reply_text("Please provide a sticker ID after /st command.")


__MODULE__ = "ꜱᴛɪᴄᴋᴇʀ ꜰɪɴᴅ"
__HELP__ = """
**sᴛɪᴄᴋᴇʀ ᴄᴏᴍᴍᴀɴᴅ**

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀʟʟᴏᴡs ᴜsᴇʀs ᴛᴏ sᴇɴᴅ sᴛɪᴄᴋᴇʀs ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ᴀ sᴛɪᴄᴋᴇʀ ID.

ғᴇᴀᴛᴜʀᴇs:
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ sᴛɪᴄᴋᴇʀ ID ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ sᴛɪᴄᴋᴇʀ.

ᴄᴏᴍᴍᴀɴᴅs:
- /st <sᴛɪᴄᴋᴇʀ_ɪᴅ>: sᴇɴᴅ ᴀ sᴛɪᴄᴋᴇʀ ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ɪᴛs ID.

ᴇxᴀᴍᴘʟᴇ:
- /sᴛ <sᴛɪᴄᴋᴇʀ_ɪᴅ>: sᴇɴᴅs ᴛʜᴇ sᴛɪᴄᴋᴇʀ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ID.

ɴᴏᴛᴇ: sᴛɪᴄᴋᴇʀ ID sᴄᴀɴ ʙᴇ ᴏʙᴛᴀɪɴᴇᴅ ғʀᴏᴍ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋs ᴏʀ ɪɴᴅɪᴠɪᴅᴜᴀʟ sᴛɪᴄᴋᴇʀs.
"""
