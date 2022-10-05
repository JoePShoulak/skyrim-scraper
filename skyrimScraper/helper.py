import json

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
    
# I really don't know how this works, but it returns a list of length-2 arrays from a list
def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)