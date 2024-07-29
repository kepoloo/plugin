import asyncio

from pyrogram import filters
from pyrogram.enums import ParseMode

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import get_assistant
from VIPMUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(
        ["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", "#"]
    )
    & SUDOERS
)
async def tag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /acancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@aall Hi Friends`"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += (
                f"\n⊚ [{m.user.first_name}](tg://openmessage?user_id={m.user.id})\n"
            )
            if usernum == 5:
                await replied.reply_text(usertxt, ParseMode.MARKDOWN)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f'\n⊚ <a href="tg://openmessage?user_id={m.user.id}">{m.user.first_name}</a>\n'

            if usernum == 5:
                await userbot.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /acancel ||",
                    ParseMode.HTML,
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        [
            "astopmention",
            "aoffall",
            "acancel",
            "aallstop",
            "astopall",
            "acancelmention",
            "aoffmention",
            "amentionoff",
            "aalloff",
            "acancelall",
            "aallcancel",
        ],
        prefixes=["/", "@", "#"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return


__MODULE__ = "Usᴇʀʙᴏᴛ Tᴀɢ"
__HELP__ = """
**Tag All Users (By Assistant)**

This command allows sudo users to tag all users in the group or channel.

Commands:
- /atag <text>: Tag all users in the group or channel with the provided text.
- /aall <text>: Tag all users in the group or channel with the provided text.
- /amention <text>: Tag all users in the group or channel with the provided text.
- /amentionall <text>: Tag all users in the group or channel with the provided text.

To stop tagging:
- /astopmention: Stop the tagging process.
- /aoffall: Stop the tagging process.
- /acancel: Stop the tagging process.
- /aallstop: Stop the tagging process.
- /astopall: Stop the tagging process.
- /acancelmention: Stop the tagging process.
- /aoffmention: Stop the tagging process.
- /amentionoff: Stop the tagging process.
- /aalloff: Stop the tagging process.
- /acancelall: Stop the tagging process.
- /aallcancel: Stop the tagging process.

Note: Only sudo users can use these commands.
"""
