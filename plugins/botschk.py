import asyncio
from datetime import datetime

from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.utils.database import get_assistant

# Assuming Userbot is defined elsewhere

last_checked_time = True


@app.on_message(filters.command("cekbot"))
async def check_bots_command(client, message):
    global last_checked_time
    try:
        # Start the Pyrogram client
        userbot = await get_assistant(message.chat.id)

        # Get current time before sending messages
        start_time = datetime.now()

        # Extract bot username from command
        command_parts = message.command
        if len(command_parts) == 2:
            bot_username = command_parts[1]
            response = ""  # Define response variable
            try:
                bot = await userbot.get_users(bot_username)
                bot_id = bot.id
                await asyncio.sleep(0.5)
                await userbot.send_message(bot_id, "/start")
                await asyncio.sleep(3)
                # Check if bot responded to /start message
                async for bot_message in userbot.get_chat_history(bot_id, limit=1):
                    if bot_message.from_user.id == bot_id:
                        response += (
                            f"╭⎋ {bot.mention}\n l\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**\n\n"
                        )
                    else:
                        response += f"╭⎋ [{bot.mention}](tg://user?id={bot.id})\n l\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
            except Exception:
                response += f"╭⎋ {bot_username}\n l\n╰⊚ **ᴇɪᴛʜᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ɢɪᴠᴇɴ ᴡʀᴏɴɢ ᴜsᴇʀɴᴀᴍᴇ ᴏᴛʜᴇʀᴡɪsᴇ ɪ ᴀᴍ ᴜɴᴀʙʟᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴅᴜᴇ ᴛᴏ ʟɪᴍɪᴛᴀᴛɪᴏɴ. **\n\n"
            # Update last checked time
            last_checked_time = start_time.strftime("%Y-%m-%d")
            await message.reply_text(f"{response}⏲️ ʟᴀsᴛ ᴄʜᴇᴄᴋ: {last_checked_time}")
        else:
            await message.reply_text(
                "ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ.\n\nᴘʟᴇᴀsᴇ ᴜsᴇ /cekbot Bot_Username\n\nʟɪᴋᴇ :- `/cekbot @AnonynmousStreamBot`"
            )
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /cekbot command: {e}")


__MODULE__ = "ʙᴏᴛꜱᴄʜᴋ"
__HELP__ = """
## Bᴏᴛs Cʜᴇᴄᴋ Cᴏᴍᴍᴀɴᴅ

### Cᴏᴍᴍᴀɴᴅ: /cekbot
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Cʜᴇᴄᴋs ᴛʜᴇ ᴏɴɪɴᴇ sᴛᴀᴛᴜs ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ʙʏ sᴇɴᴅɪɴɢ ɪᴛ ᴀ /sᴛᴀʀᴛ ᴍᴇssᴀɢᴇ.

**Usᴀɢᴇ:**
/cekbot Bᴏᴛ_Usᴇʀɴᴀᴍᴇ

**Dᴇᴛᴀɪs:**
- Sᴇɴᴅs /sᴛᴀʀᴛ ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋs ɪғ ɪᴛ ʀᴇsᴘᴏɴᴅs.
- Dɪsᴘʟᴀʏs ᴛʜᴇ ʙᴏᴛ's sᴛᴀᴛᴜs ᴀs ᴇɪᴛʜᴇʀ ᴏɴɪɴᴇ ᴏʀ ᴏғғʟɪɴᴇ.

**Exᴀᴍᴘᴇs:**
- /cekbot @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ: Cʜᴇᴄᴋs ɪғ @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ ɪs ᴏɴʟɪɴᴇ ᴏʀ ᴏғғɪʟɴᴇ.

**Nᴏᴛᴇs:**
- Tʜᴇ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ ᴍᴜsᴛ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴀs ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ.
- Tʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴅɪsᴘʟᴀʏ ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ɪғ ᴛʜᴇ ᴜsᴇʀɴᴀᴍᴇ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ ᴏʀ ɪғ ᴛʜᴇʀᴇ ᴀʀᴇ ɪᴍɪᴛᴀᴛɪᴏɴs.

**Oᴜᴛᴘᴜᴛ:**
- Dɪsᴘʟᴀʏs ᴛʜᴇ ʙᴏᴛ's ᴍᴇɴᴛɪᴏɴ ᴀɴᴅ ɪᴛs ᴏɴʟɪɴᴇ sᴛᴀᴛᴜs.
- Sʜᴏᴡs ᴛʜᴇ ᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴛɪᴍᴇ.
"""
