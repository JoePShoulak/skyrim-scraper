import scrapy

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
                    "base_cost": data[0][4:-5],
                    "base_mag": data[1][4:-5],
                    "base_dur": data[2][4:-5]
                }