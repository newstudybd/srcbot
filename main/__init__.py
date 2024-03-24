#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22506688
API_HASH = "e210ba8b245fffbaa7af50a901c6bee8"
BOT_TOKEN = "7057913309:AAFcSx8CR-EveyMXrXHoWOQh2EFBOPE0Qzg"
SESSION = "BQFXbMAAMc2Ce2PlL9RBJ7QSLJyLw6voM7pweQphsKqy2emmpq4ep0iJTZAVudZsEfQT6d1pnQolywLWRE4ssAsZAOOrMTsVlCe2XQzuWWqSPZZGDVWnBKKgERoIH07OP8yOfws4xTY3vUWUnO8vsyhdTASJ0QLgirXI5jUBdYH6Msvaw50feC8dJ1xnBZGWD3pw4zLsgRwBDl0hhOyNg113XVgQ_U9ADI_qcYCaBd_Gkuzt7cdZX6uH3sPEfnqnOcZK_Z6eoIvh3oKvAUQehT6hAEiTNndl8t24jpKY-zCsCoFMUGnenxODQRehcXknFCYZw2d-rLar8MYF1CVCCrGLMtMF9QAAAAGbj763AA"
AUTH = 6303728812

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
