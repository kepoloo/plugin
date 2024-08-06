from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import enums, filters
from pyrogram.types import (
    CallbackQuery,
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from VIPMUSIC import app
from VIPMUSIC.mongo.nightmodedb import (
    get_nightchats,
    nightdb,
    nightmode_off,
    nightmode_on,
)

CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_send_polls=False,
    can_change_info=False,
    can_add_web_page_previews=False,
    can_pin_messages=False,
    can_invite_users=True,
)


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_send_polls=True,
    can_change_info=True,
    can_add_web_page_previews=True,
    can_pin_messages=True,
    can_invite_users=True,
)

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ ᴇɴᴀʙʟᴇ ๏", callback_data="add_night"),
            InlineKeyboardButton("๏ ᴅɪsᴀʙʟᴇ ๏", callback_data="rm_night"),
        ]
    ]
)
add_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="๏ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ๏",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ]
    ]
)


@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(
        photo="https://telegra.ph//file/2ca21769aa93db06cf773.jpg",
        caption="**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ɴɪɢʜᴛᴍᴏᴅᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**",
        reply_markup=buttons,
    )


@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id": chat_id})
    administrators = []
    async for m in app.get_chat_members(
        chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        administrators.append(m.user.id)
    if user_id in administrators:
        if data == "add_night":
            if check_night:
                await query.message.edit_caption(
                    "**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**"
                )
            elif not check_night:
                await nightmode_on(chat_id)
                await query.message.edit_caption(
                    "**๏ ᴀᴅᴅᴇᴅ ᴄʜᴀᴛ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ . ᴛʜɪs ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ᴄʟᴏsᴇᴅ ᴏɴ 𝟷𝟸ᴀᴍ [IST] ᴀɴᴅ ᴡɪʟʟ ᴏᴘᴇɴᴇᴅ ᴏɴ 𝟶𝟼ᴀᴍ [IST] .**"
                )
        if data == "rm_night":
            if check_night:
                await nightmode_off(chat_id)
                await query.message.edit_caption(
                    "**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ !**"
                )
            elif not check_night:
                await query.message.edit_caption(
                    "**๏  ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ  ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**"
                )


async def start_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://telegra.ph//file/2ca21769aa93db06cf773.jpg",
                caption=f"**ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs.\n\nɢʀᴏᴜᴘ ɪs ᴄʟᴏsɪɴɢ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴇᴠᴇʀʏᴏɴᴇ  !**",
                reply_markup=add_buttons,
            )

            await app.set_chat_permissions(add_chat, CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")


scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()


async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption=f"**ɢʀᴏᴜᴘ ɪs ᴏᴘᴇɴɪɴɢ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ !\n\nᴍᴀʏ ᴛʜɪs ᴅᴀʏ ᴄᴏᴍᴇ ᴡɪᴛʜ ᴀʟʟ ᴛʜᴇ ʟᴏᴠᴇ ʏᴏᴜʀ ʜᴇᴀʀᴛ ᴄᴀɴ ʜᴏʟᴅ ᴀɴᴅ ʙʀɪɴɢ ʏᴏᴜ ᴇᴠᴇʀʏ sᴜᴄᴄᴇss ʏᴏᴜ ᴅᴇsɪʀᴇ. Mᴀʏ ᴇᴀᴄʜ ᴏғ ʏᴏᴜʀ ғᴏᴏᴛsᴛᴇᴘs ʙʀɪɴɢ Jᴏʏ ᴛᴏ ᴛʜᴇ ᴇᴀʀᴛʜ ᴀɴᴅ ʏᴏᴜʀsᴇʟғ. ɪ ᴡɪsʜ ʏᴏᴜ ᴀ ᴍᴀɢɪᴄᴀʟ ᴅᴀʏ ᴀɴᴅ ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ʟɪғᴇ ᴀʜᴇᴀᴅ.**",
                reply_markup=add_buttons,
            )
            await app.set_chat_permissions(rm_chat, OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")


scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()

__MODULE__ = "Nɪɢʜᴛᴍᴏᴅᴇ"
__HELP__ = """
## Nɪɢʜᴛᴍᴏᴅᴇ Cᴏᴍᴍᴀɴᴅs Hᴇᴘ

### 1. /ɴɪɢʜᴛᴍᴏᴅᴇ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Eɴᴀʙᴇ ᴏʀ ᴅɪsᴀʙᴇ ɴɪɢʜᴛᴍᴏᴅᴇ ɪɴ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.

**Usᴀɢᴇ:**
/ɴɪɢʜᴛᴍᴏᴅᴇ

**Dᴇᴛᴀɪs:**
- Eɴᴀʙᴇs ᴏʀ ᴅɪsᴀʙᴇs ɴɪɢʜᴛᴍᴏᴅᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
- Nɪɢʜᴛᴍᴏᴅᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʏ ᴄᴏsᴇs ᴛʜᴇ ᴄʜᴀᴛ ᴅᴜʀɪɴɢ ɴɪɢʜᴛ ʜᴏᴜʀs (12:00 AM ᴛᴏ 6:00 AM) ᴀɴᴅ ᴏᴘᴇɴs ɪᴛ ɪɴ ᴛʜᴇ ᴍᴏʀɴɪɴɢ.
- Oɴʏ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴄᴀɴ ᴇɴᴀʙᴇ ᴏʀ ᴅɪsᴀʙᴇ ɴɪɢʜᴛᴍᴏᴅᴇ.
- Usᴇʀs ᴄᴀɴ ᴄɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴇɴᴀʙᴇ ᴏʀ ᴅɪsᴀʙᴇ ɴɪɢʜᴛᴍᴏᴅᴇ.

**Exᴀᴍᴘᴇs:**
- `/ɴɪɢʜᴛᴍᴏᴅᴇ`

"""
