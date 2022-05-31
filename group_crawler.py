import requests
import json


def telegram_search():
    word = "altcoin"  # input("What you search?\n")
    response = requests.get(f"https://telegramchannels.me/search?search={word}&type=group")
    print(type(response))
    print(dir(response))
    print(response.json())
    # resp_dict = json.loads(response.text)
    # print(resp_dict)
    return response


if __name__ == '__main__':
    telegram_search()
