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

print("𝚜𝚝𝚊𝚛𝚝𝚒𝚗𝚐 𝚜𝚞𝚒𝚌𝚒𝚍𝚎 𝚋𝚘𝚝 𝚜𝚎𝚛𝚟𝚎𝚛....") 

"""
𝚖𝚘𝚟𝚒𝚗𝚐 𝚝𝚘 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚗𝚘𝚠.... 
"""

Lund = []
for x in Var.OWNER_ID: 
    Lund.append(x)


@hero.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in Lund:
        start = datetime.now()
        text = "𝚋𝚘𝚗𝚐𝚞...."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**𝚒𝚊𝚖 𝚊𝚌𝚝𝚒𝚟𝚎 😒\n𝚜𝚝𝚊𝚛𝚝 𝚏𝚞𝚌𝚔𝚒𝚗𝚐 𝚊𝚗𝚢 𝚐𝚛𝚘𝚞𝚙** \n\n **__𝙱𝚘𝚗𝚐𝚞😏__** `{ms}` ms")

"""
 𝚁𝚎𝚜𝚝𝚊𝚛𝚝 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜.... 
"""
@hero.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in Lund:
        text = "𝙸𝚊𝚖 𝚁𝚎𝚊𝚍𝚢 𝚝𝚘 𝙵𝚞𝚌𝚔 𝚃𝚊𝚛𝚐𝚎𝚝𝚎𝚍 𝚐𝚛𝚘𝚞𝚙𝚜...."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await hero.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 𝚜𝚞𝚒𝚌𝚒𝚍𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍... 
"""
 
@hero.on(events.NewMessage(pattern="^/suicide"))
async def testing(event):
  if event.sender_id in Lund:
   if not event.is_group:
        Reply = f"𝙽𝚘𝚘𝚋 𝚞𝚜𝚎 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚒𝚗 𝚐𝚛𝚘𝚞𝚙..."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       veer = await event.get_chat()
       veerA = await event.client.get_me()
       admin = veer.admin_rights
       creator = veer.creator
       if not admin and not creator:
           await event.reply("𝙸 𝚍𝚘𝚗'𝚝 𝚑𝚊𝚟𝚎 𝚜𝚞𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝 𝚁𝚒𝚐𝚑𝚝𝚜...")
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
