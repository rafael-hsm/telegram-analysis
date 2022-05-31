from bs4 import BeautifulSoup
import requests


def get_html(url):
    resp = requests.get(url)
    return resp.text


def get_urls(html, starting_string):
    soup = BeautifulSoup(html)
    all_urls = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith(starting_string):
            all_urls.append(url)
    return all_urls


get_new_currency_resp = requests.get("https://coinmarketcap.com/new/")

get_new_currency_html = get_new_currency_resp.text
all_coin_urls = get_urls(get_new_currency_html, "/currencies")
telegram_groups = []

for coin_url in all_coin_urls:
    coin_url = "https://coinmarketcap.com" + coin_url
    coin_html = get_html(coin_url)
    all_telegram_urls = get_urls(coin_html, "https://t.me")
    telegram_groups = telegram_groups + all_telegram_urls

    clean_telegram_list = []
    for telegram_group in telegram_groups:
        if not "CoinMarketCap" in telegram_group:
            clean_telegram_list.append(telegram_group)

print(clean_telegram_list)
