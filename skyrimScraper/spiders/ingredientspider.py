from xml.etree.ElementInclude import include
import scrapy

def parsedUrl(dataRow, index=1):
    return "https://en.uesp.net" + dataRow.css('a').getall()[index].split(" ")[1].split("=")[1].replace('"', '')

# I really don't know how this works, but it returns a list of tuples from a list
def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

class IngredientSpider(scrapy.Spider):
    name = 'ingredients'
    start_urls = ['https://en.uesp.net/wiki/Skyrim:Ingredients']

    def parse(self, response):
        tablerows = response.css('.wikitable')[0].css('tr')[1:]

        for row1, row2 in pairwise(tablerows):
            effect_names = row2.css('a::text').getall()

            yield {
                "name": row1.css('a::text').get(),
                "url": parsedUrl(row1),

                "effect1_name": effect_names[0],
                "effect2_name": effect_names[1],
                "effect3_name": effect_names[2],
                "effect4_name": effect_names[3],

                "effect1_url": parsedUrl(row2, 1),
                "effect2_url": parsedUrl(row2, 2),
                "effect3_url": parsedUrl(row2, 3),
                "effect4_url": parsedUrl(row2, 4)
            }