# -*- coding: utf-8 -*-
import scrapy


class StoriesSpider(scrapy.Spider):
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
        harmed_people = response.xpath('//cite/text()').extract()[1].strip()

        yield {
            'topic': response.meta.get('topic'),
            'harmed_people': harmed_people
        }
