import scrapy

from ..helper import textFromElement

class EffectSpider(scrapy.Spider):
    name = 'effects'
    start_urls = ['https://en.uesp.net/wiki/Skyrim:Alchemy_Effects']

    def parse(self, response):
        table = response.css('.sortable').css('tr')

        for row in table:
            name = row.css('a::text').get()
            
            id = "".join(row.css('.idall span::text').getall())

            data = row.css('td').getall()[2:]

            if data == []:
                pass
            else:   
                yield {
                    "name": name,
                    "id": id,
                    "base_cost": textFromElement(data[0]),
                    "base_mag": textFromElement(data[1]),
                    "base_dur": textFromElement(data[2])
                }