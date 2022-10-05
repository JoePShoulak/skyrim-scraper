import scrapy, json

# lol
def bigPrint(string):
    print()
    print(string)
    print()

# Grab the URLs we already stored using out linkSpider
def getIngredientURLS():
    f = open('link_data.json')
    data = json.load(f)

    urls = list(map(lambda x: x['url'], data))

    return urls

# Make sure the link we're looking at is an effect link (by eliminiation)
def checkEffectLink(link):
    badContent = [".png", "Form_ID", "Hearthfire", "Dawnguard", "Dragonborn", "Alchemy"]

    for thing in badContent:
        if thing in link:
            return False

    return True

# Quick and dirty way to grab an attr from a DOM element
def getAttr(element, attr):
    return element.split(attr + "=")[1].split(" ")[0]


# Because these lazy programmers didn't include proper classing in their HTML, we have to do some gross parsing
def parsedUrl(dataRow, index=1):
    link = dataRow.css('a').getall()[index]
    url = getAttr(link, "href").replace('"', '')

    return "https://en.uesp.net" + url

class IngredientDataSpider(scrapy.Spider):
    name = 'ingredient_data'
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
            "name": table.css('a').attrib['title'],
            "id": id,
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