# (©)Codexbotz
# Recode by @xflskyura
# t.me/KyuraxStore & t.me/KyuraSupportGroup

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "xyreynld")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>ʜɪ sᴀɢᴀᴘᴜɴɢ {first}</b>\n\n<b>ɢᴜᴇ ʙɪsᴀ sɪᴍᴘᴇɴ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʟᴏ ᴛʀᴜs ʙɪsᴀ ᴅɪ ᴀᴋsᴇs sᴀᴍᴀ sɪ ᴋᴏɴᴛᴏʟ ᴘᴀᴋᴇ ʟɪɴᴋ.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>ʜɪ ᴋᴏɴᴛᴏʟ {first}\n\nʟᴏ ʜᴀʀᴜs ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴏᴜᴘ ɢᴜᴇ sᴜᴘᴀʏᴀ ʙɪsᴀ ᴅᴀᴘᴇᴛ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ ɴʏᴀ\n\nᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴏᴜᴘ ᴅᴜʟᴜ ʏᴀ ᴋᴏɴᴛᴏʟ</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((5263211098, 5409900061, 5415571049, 5530935977))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
