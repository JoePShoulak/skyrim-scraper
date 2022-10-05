import scrapy

from ..helper import pairwise, parsedUrl

class LinkSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://en.uesp.net/wiki/Skyrim:Ingredients']

    def parse(self, response):
        tablerows = response.css('.wikitable')[0].css('tr')[1:]

        for row1, _ in pairwise(tablerows):

            yield {
                "name": row1.css('a::text').get(),
                "url": parsedUrl(row1)
            }