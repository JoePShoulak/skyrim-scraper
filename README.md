# skyrim-scraper
A simple scrapy scraper to grab info from Skyrim Wikis, mainly that for crafting (Alchemy, Smithing, Enchanting, Cooking)

## Use ##

Run `scrapy crawl links -O link_data.json` to generate the link data that will be handled by the next spider. 

Run `scrapy crawl ingredients -O ingredient_data.json` to crawl through those links and save out all the data we can currently grab from the wiki. 

Run `scrapy crawl effect -O effect_data.json` to crawl through the list of effects and grab the relevant data.
