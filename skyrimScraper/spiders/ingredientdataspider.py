import scrapy

from ..helper import getIngredientURLS, parsedUrl, checkEffectLink

class IngredientDataSpider(scrapy.Spider):
    name = 'ingredients'
    start_urls = getIngredientURLS()

    def parse(self, response):
        table = response.css('.infobox')

        id = "".join(table.css(".idall span::text").getall())

        data = table.css('td::text').getall()
        effects = table.css('a::text').getall()

        links = table.css('a')
        parsedlinks = []

        for i in range(len(links)):
            parsedlinks += [parsedUrl(links, i)]

        parsedlinks = list(filter(checkEffectLink, parsedlinks))[:8]
        
        effects = effects[1:5]

        yield {
            # TODO: Grab Icon URLs
            # TODO: Grab modifier values (magnitude, duration, value) per effect

            "name": table.css('a').attrib['title'],
            "id": id.upper(),
            "value": data[0],
            "weight": data[1],

            "effect1_name": effects[0],
            "effect2_name": effects[1],
            "effect3_name": effects[2],
            "effect4_name": effects[3],

            "effect1_url": parsedlinks[0],
            "effect2_url": parsedlinks[2],
            "effect3_url": parsedlinks[4],
            "effect4_url": parsedlinks[6],
        }