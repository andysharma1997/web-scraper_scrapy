# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VedantuScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    table_data = scrapy.Field()
    dev_text = scrapy.Field()
    p_text = scrapy.Field()
    url = scrapy.Field()
    page_links = scrapy.Field()



