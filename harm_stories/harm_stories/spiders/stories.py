# -*- coding: utf-8 -*-
import scrapy


class StoriesSpider(scrapy.Spider):
    name = 'stories'
    allowed_domains = ['http://whatstheharm.net/index.html']
    start_urls = ['http://http://whatstheharm.net/index.html/']

    def parse(self, response):
        pass
