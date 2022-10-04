import scrapy

class IngredientSpider(scrapy.Spider):
    name = 'ingredients'
    start_urls = ['https://en.uesp.net/wiki/Skyrim:Ingredients']

    def parse(self, response):
        tablerows = response.css('.wikitable tr')[1:-1]

        for tablerow in tablerows:
            yield {
                "data": tablerow.css('a::text').get()
                }