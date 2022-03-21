from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/d257ba98dbd40a7f6fa04.jpg",
                caption="✨ **Kayzu Ubot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @kayzuchannel ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/KayzuSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
