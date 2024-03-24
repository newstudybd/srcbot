#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 13402873
API_HASH = "457bfe39a36ed5ab036c9e7536ed0307"
BOT_TOKEN = "6767554779:AAFD65XssBLPcQ3LIbh2zmXiceTWk0D3lLo"
SESSION = "BQDMgvkAFIKSSn1QVmzA0fNZiUsxpW_kFEsdhkVBKjPY-pVhKOSoZZ4v71wzmcVD5s2p5Fofb1MYi6IwmD5Vzqwmp9f6nrKTVYExXmHfzw-gonAbIIXtWNAK_j7JM9-pr82GHRVh4063sIdUklOJlteVJ0E87wDHcMJiQpcE0GjCw2QAUkI8qwp0pvtI3SAyBaEafaaHG-kENiVzIFE5NFVoOEAbLILzWVXNoBtlamz5xqkbsJmyqGx9PwN-wTH_m1vCcDtGldRFCjiIOuiXnhU0esJGuhK1w8In38bRYjeDgiiMDNkeeLQbI2UvTvstiENF-QXbdx2owSL_kbXf41NL7akHMwAAAAF-FBhiAA"
AUTH = 5193190005

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
