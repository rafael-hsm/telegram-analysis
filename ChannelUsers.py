import configparser
import json
import asyncio

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (PeerChannel)
import pandas as pd

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
# Access this for get our api_id and api_hash https://my.telegram.org/
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)


async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    user_input_channel = input("enter entity(telegram URL or entity id):")

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    offset = 0
    limit = 100
    all_participants = []

    while True:

        participants = await client(
            GetParticipantsRequest(my_channel, ChannelParticipantsSearch(''), offset, limit, hash=0, aggressive=True))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    all_user_details = []
    for participant in all_participants:
        all_user_details.append(
            {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
             "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})

    with open('user_data.json', 'w') as outfile:
        json.dump(all_user_details, outfile)

    print(all_user_details)
    print(len(all_user_details))
    print(type(all_user_details))
    df_1 = pd.DataFrame(all_user_details, columns=['id', 'first_name', 'phone', 'is_bot'])
    print(df_1.info())
    df_1.to_csv("user_channel.csv")
    print(f"Total members: {df_1.shape[0]}")
    total_bots = df_1['is_bot'].value_counts()
    print(f"True = bots\n{total_bots}")


with client:
    # https://t.me/coinsnipernet
    # https://t.me/ENJINSTARTER
    # https://t.me/apolloxchange
    # https://t.me/RebaseAPY_chat
    client.loop.run_until_complete(main(phone))
