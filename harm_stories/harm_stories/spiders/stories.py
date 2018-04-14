# -*- coding: utf-8 -*-
import scrapy


class StoriesSpider(scrapy.Spider):
    name = 'stories'
    start_urls = ['http://whatstheharm.net/index.html']

    def parse(self, response):
        table = response.xpath('//table')[1]
        topics = table.xpath('.//a/text()').extract()

        for topic in topics:
            yield {
                'topic': topic,
            }
