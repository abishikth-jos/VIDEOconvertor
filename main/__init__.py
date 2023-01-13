from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=3264452, cast=int)
API_HASH = config("API_HASH", default="dfa13ad72701f1bbaba18eb59fd52df3" )
BOT_TOKEN = config("BOT_TOKEN", default="1682428637:AAEvh8KYBqFANnqEFag5prl8W0xu2-MP9K0" )
BOT_UN = config("BOT_UN", default="@Encoder_Ts_bot")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
