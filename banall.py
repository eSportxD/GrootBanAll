from client import Var
import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


hero = TelegramClient(None, Var.API_KEY, Var.API_HASH)
hero.start(bot_token=Var.TOKEN)

print("𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂 𝘽𝘼𝙉𝘼𝙇𝙇 𝘽𝙊𝙏 𝙎𝙀𝙍𝙑𝙀𝙍....") 

"""
𝙈𝙊𝙑𝙄𝙉𝙂 𝙏𝙊 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𝙉𝙊𝙒.... 
"""

Lund = []
for x in Var.OWNER_ID: 
    Lund.append(x)


@hero.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in Lund:
        start = datetime.now()
        text = "𝙋𝙤𝙣𝙜...."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**𝙄'𝙢 𝘼𝙘𝙩𝙞𝙫𝙚🔥\n𝙎𝙩𝙖𝙧𝙩 𝙁𝙪𝙘𝙠𝙞𝙣𝙜 𝘼𝙣𝙮 𝙂𝙧𝙤𝙪𝙥** \n\n **__ᏢᎾᏁᎶ🏓__** `{ms}` ms")

"""
 𝙍𝙀𝙎𝙏𝘼𝙍𝙏 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎.... 
"""
@hero.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in Lund:
        text = "𝙄 𝙖𝙢 𝙧𝙚𝙖𝙙𝙮 𝙩𝙤 𝙛𝙪𝙘𝙠 𝙩𝙖𝙧𝙜𝙚𝙩𝙚𝙙 𝙜𝙧𝙤𝙪𝙥𝙨...."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await hero.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 𝘽𝘼𝙉𝘼𝙇𝙇 𝘾𝙊𝙈𝙈𝘼𝙉𝘿... 
"""
 
@hero.on(events.NewMessage(pattern="^/suicide"))
async def testing(event):
  if event.sender_id in Lund:
   if not event.is_group:
        Reply = f"𝙉𝙤𝙤𝙗 𝙐𝙨𝙚 𝙏𝙝𝙞𝙨 𝘾𝙢𝙙 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥..."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       veer = await event.get_chat()
       veerA = await event.client.get_me()
       admin = veer.admin_rights
       creator = veer.creator
       if not admin and not creator:
           await event.reply("𝙄 𝘿𝙤𝙣'𝙩 𝙝𝙖𝙫𝙚 𝙨𝙪𝙛𝙛𝙞𝙘𝙞𝙚𝙣𝙩 𝙧𝙞𝙜𝙝𝙩𝙨...")
           return
       await event.reply("**𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙛𝙪𝙘𝙠𝙞𝙣𝙜 𝙩𝙝𝙞𝙨 𝙜𝙧𝙤𝙪𝙥...**")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == veerA.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


print("𝙇𝙚𝙖𝙫𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝙎𝙤𝙤𝙣 𝘾𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝘼𝙢 𝘽𝙪𝙨𝙮") 
print("𝙎𝙏𝘼𝙍𝙏𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇𝙇𝙔...") 
hero.run_until_disconnected()
