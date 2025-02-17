# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from most_popular_movies.items import NomineeItem
from scrapy import Spider


class OscarsSpider(Spider):
    name = 'oscars'
    start_urls = ['https://www.oscars.org/oscars/ceremonies/2025']

    def parse(self, response):
        main_section = response.xpath("//div[contains(@class, 'field--name-field-award-categories')]")
        items = main_section.xpath("div[contains(@class, 'field__item')]")

        for item in items:
            category = item.xpath(".//div[contains(@class, 'field--name-field-award-category-oscars')]/text()").get()
            loader = ItemLoader(item=NomineeItem(), response=response)
            loader.add_value('category', category)

            nominees = item.xpath(".//div[contains(@class, 'paragraph--type--award-honoree')]")
            parsed_nominees = nominees.css(".field__item")[::2]

            for nom in parsed_nominees:
                nominee_text = nom.xpath("text()").get()
                loader.add_value('nominees', nominee_text)

            yield loader.load_item()
