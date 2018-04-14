# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from harm_stories.items import HarmStoriesItem
from scrapy import Spider


class StoriesSpider(Spider):
    name = 'stories'
    start_urls = ['http://whatstheharm.net/index.html']

    def parse(self, response):
        table = response.xpath('//table')[1]
        links = table.xpath('.//a')

        for link in links:
            topic = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()

            yield response.follow(
                    href,
                    callback=self.parse_story,
                    meta={ 'topic': topic }
        )

    def parse_story(self, response):
        loader = ItemLoader(item=HarmStoriesItem(), response=response)
        harmed_people = response.xpath('//cite/text()').extract()[1].strip()

        loader.add_value('topic', response.meta.get('topic'))
        loader.add_value('harmed_people', harmed_people)

        return loader.load_item()
