import scrapy

# Quick and dirty way to grab an attr from a DOM element
def getAttr(element, attr):
    return element.split(attr + "=")[1].split(" ")[0]

# Because these lazy programmers didn't include proper classing in their HTML, we have to do some gross parsing
def parsedUrl(dataRow, index=1):
    link = dataRow.css('a').getall()[index]
    url = getAttr(link, "href").replace('"', '')

    return "https://en.uesp.net" + url

# I really don't know how this works, but it returns a list of length-2 arrays from a list
def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

class LinkSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://en.uesp.net/wiki/Skyrim:Ingredients']

    def parse(self, response):
        tablerows = response.css('.wikitable')[0].css('tr')[1:]

        for row1, row2 in pairwise(tablerows):
            effect_names = row2.css('a::text').getall()

            yield {
                "name": row1.css('a::text').get(),
                "url": parsedUrl(row1),

                # "effect1_name": effect_names[0],
                # "effect2_name": effect_names[1],
                # "effect3_name": effect_names[2],
                # "effect4_name": effect_names[3],

                # "effect1_url": parsedUrl(row2, 1),
                # "effect2_url": parsedUrl(row2, 2),
                # "effect3_url": parsedUrl(row2, 3),
                # "effect4_url": parsedUrl(row2, 4)
            }