import scrapy, json, os

def getIngredientURLS():
    f = open('data.json')
    data = json.load(f)

    urls = list(map(lambda x: x['url'], data))

    return urls

class IngredientDataSpider(scrapy.Spider):
    name = 'ingredient_data'
    start_urls = getIngredientURLS()

    def parse(self, response):
        table = response.css('.infobox')

        name = table.css('a').attrib['title']

        data = table.css('td::text').getall()
        value = data[0]
        weight = data[1]

        links = table.css('a::text').getall()
        print(links)
        effects = links[1:]
        if len(effects) > 4:
            effects = effects[:-1]


        yield {
            "name": name,
            "value": value,
            "weight": weight,

            "effect1_name": effects[0],
            "effect2_name": effects[1],
            "effect3_name": effects[2],
            "effect4_name": effects[3],
        }