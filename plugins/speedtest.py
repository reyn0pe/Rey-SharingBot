#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
# Ported by @mrismanaziz
# FROM File-Sharing-Man < https://github.com/mrismanaziz/File-Sharing-Man/ >
# t.me/Lunatic0de & t.me/SharingUserbot
#

import os

import speedtest
import wget
from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS


@Bot.on_message(filters.command("speedtest") & filters.user(ADMINS))
async def run_speedtest(client: Bot, message: Message):
    m = await message.reply_text("Sabar Dikit Ya Memek...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("Gue Bilang Sabar Ya Sabar Babi...")
        test.download()
        m = await m.edit("Etdah Bentaran Memek...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("NOH UDAH KONTOL")
    path = wget.download(result["share"])

    output = f"""✪ <b>Hasil SpeedTest</b>
    
𐁍 <u><b>Client:<b></u>
𐁍 <b>ISP:</b> {result['client']['isp']}
𐁍 <b>Country:</b> {result['client']['country']}
  
𐁍 <u><b>Server:</b></u>
𐁍 <b>Name:</b> {result['server']['name']}
𐁍 <b>Country:</b> {result['server']['country']}, {result['server']['cc']}
𐁍 <b>Sponsor:</b> {result['server']['sponsor']}
𐁍️ <b>Ping:</b> {result['ping']}"""
    msg = await client.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
