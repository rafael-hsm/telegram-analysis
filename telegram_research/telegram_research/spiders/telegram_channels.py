import scrapy


class TelegramChannelsSpider(scrapy.Spider):
    name = 'telegram_channels'
    start_urls = ['https://telegramchannels.me/search?search=bitcoin&type=group']

    def parse(self, response):
        name = response.css(".is-size-6.two-line-text")
        total_members = response.css(".media-content .is-size-7")
        link = response.css(".has-text-grey-darker .card-content")
        pass
