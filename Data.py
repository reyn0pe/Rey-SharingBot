# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode by @reyn0pe

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> β£ π’ππππΊππ½ π»ππΊπ ππΊππΎ π»ππ πππΊ
βββββββββββββββββββββ
    /start - Mulai bot
    /about - Tentang bot
    /help - Bantuan bot
    /ping - Cek bot
    /uptime - Status bot
βββββββββββββββββββββ
 
 β£ Command buat admin bot
βββββββββββββββββββββ
    /logs - Untuk melihat logs bot
    /setvar - Untuk mengatur var dengan command dibot
    /delvar - Untuk menghapus var dengan command dibot
  β΄ /getvar - Untuk melihat salah satu var dengan command dibot
    /users - Untuk melihat statistik pengguna bot
    /batch - Untuk membuat link lebih dari satu file
    /speedtest - Untuk Mengetes kecepatan server bot
    /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

β Develoved by </b><a href='https://t.me/xyreynld'>@ReyKulbet</a>
"""

    close = [
        [InlineKeyboardButton("Β» α΄α΄α΄α΄α΄ Β«", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Β» Κα΄Κα΄ Β«", callback_data="help"),
            InlineKeyboardButton("Β» α΄α΄α΄α΄α΄ Β«", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("Β» α΄α΄Ι΄α΄α΄Ι΄Ι’ sα΄Κα΄ Β«", callback_data="about"),
            InlineKeyboardButton("Β» α΄α΄α΄α΄α΄ Β«", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 β’ Creator: @{}
 β’ Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 β’ Source Code: <a href='https://github.com/reyn0pe/Rey-SharingBot'>Rey-SharingBot</a>

β Develoved by </b><a href='https://t.me/xyreynld'>@ReyKulbet</a>
"""
