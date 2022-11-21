# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode by @reyn0pe

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ✣ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖻𝗎𝖺𝗍 𝗉𝖺𝗄𝖾 𝖻𝗈𝗍 𝗇𝗒𝖺
━━━━━━━━━━━━━━━━━━━━━
    /start - Mulai bot
    /about - Tentang bot
    /help - Bantuan bot
    /ping - Cek bot
    /uptime - Status bot
━━━━━━━━━━━━━━━━━━━━━
 
 ✣ Command buat admin bot
━━━━━━━━━━━━━━━━━━━━━
    /logs - Untuk melihat logs bot
    /setvar - Untuk mengatur var dengan command dibot
    /delvar - Untuk menghapus var dengan command dibot
  ╴ /getvar - Untuk melihat salah satu var dengan command dibot
    /users - Untuk melihat statistik pengguna bot
    /batch - Untuk membuat link lebih dari satu file
    /speedtest - Untuk Mengetes kecepatan server bot
    /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

♛ Develoved by </b><a href='https://t.me/xyreynld'>@ReyKulbet</a>
"""

    close = [
        [InlineKeyboardButton("» ᴛᴜᴛᴜᴘ «", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("» ʜᴇʟᴘ «", callback_data="help"),
            InlineKeyboardButton("» ᴛᴜᴛᴜᴘ «", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("» ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ «", callback_data="about"),
            InlineKeyboardButton("» ᴛᴜᴛᴜᴘ «", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://github.com/reyn0pe/Rey-SharingBot'>Rey-SharingBot</a>

♛ Develoved by </b><a href='https://t.me/xyreynld'>@ReyKulbet</a>
"""
