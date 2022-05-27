import configparser

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

# Reading Configs
# Access this for get our api_id and api_hash https://my.telegram.org/
config = configparser.ConfigParser()
config.read("../config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins

target_groups = ['https://t.me/fimimarket', 'https://t.me/FimiAnnouncements', 'https://t.me/catcoiner',
                 'https://t.me/catcoiner', 'https://t.me/multiplanetaryinus', 'https://t.me/multiplanetaryinus',
                 'https://t.me/alyattesofficial', 'https://t.me/alyattes_tr', 'https://t.me/kinja_eth',
                 'https://t.me/kinja_eth', 'https://t.me/lasereyestoken', 'https://t.me/lasereyestoken',
                 'https://t.me/Chinazilla_official', 'https://t.me/Chinazilla_official', 'https://t.me/warenachat',
                 'https://t.me/warenaOfficial, https://www.instagram.com/warenaofficial/',
                 'https://t.me/KingdomKarnage', 'https://t.me/KingdomKarnage', 'https://t.me/partyboard_en',
                 'https://t.me/ApeFund', 'https://t.me/ApeFund', 'https://t.me/SHIBA2K22', 'https://t.me/SHIBA2K22',
                 'https://t.me/Chiba_inu1', 'https://t.me/Chiba_inu1', 'https://t.me/solventprotocol',
                 'https://t.me/SperaxUSD', 'https://t.me/realdogelana', 'https://t.me/SmartShibaOfficial',
                 'https://t.me/shibaxdefi', 'https://t.me/defibayofficial', 'https://t.me/defibayofficial',
                 'https://t.me/coinfreshofficial', 'https://t.me/coinfreshofficial', 'https://t.me/placewar',
                 'https://t.me/InuWarsLiquidation', 'https://t.me/InuWarsLiquidation', 'https://t.me/harmonyplayone',
                 'https://t.me/shibatoby', 'https://t.me/shibatoby']

telegram_group_names = []
for item in target_groups:
    telegram_group_names.append(item.replace("https://t.me/", ""))
print(telegram_group_names)

for target_group in telegram_group_names:
    try:

        client(JoinChannelRequest(target_group))
        all_participants = client.get_participants(target_group, aggressive=True, filter=ChannelParticipantsAdmins)

        for user in all_participants:
            receiver = user.username
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()

            client.send_message(receiver, "Hey {}, What's the contract address for {}".format(name, target_group))
            print("message sent to {}".format(receiver))
    except Exception as e:
        print("Error: {}".format(e))
