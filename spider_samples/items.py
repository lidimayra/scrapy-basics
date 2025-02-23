# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    summary = Field()
    director = Field()

class NomineeItem(Item):
    category = Field()
    nominees = Field()
