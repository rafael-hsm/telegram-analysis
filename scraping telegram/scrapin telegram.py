from bs4 import BeautifulSoup
import requests

search_word = input("What do you search?\n")
html = requests.get("https://telegramchannels.me/search?search=%d&type=group".format(search_word)).content
soup = BeautifulSoup(html, 'html.parser')
print(html)
print(soup)
print(soup.prettify())
