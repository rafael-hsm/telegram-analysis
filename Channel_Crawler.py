import configparser

from telethon.sync import TelegramClient
from telethon import functions, types

# Reading Configs
# Access this for get our api_id and api_hash https://my.telegram.org/
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.channels.GetChannelsRequest(
        id=['username']
    ))
    print(result.stringify())
