# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from most_popular_movies.items import MovieItem
from scrapy import Spider


class MoviesSpider(Spider):
    name = 'movies'
    start_urls = ['https://www.imdb.com/chart/moviemeter']

    def parse(self, response):
        tbody = response.xpath("//tbody[contains(@class, 'lister-list')]")
        data_columns = tbody.xpath("//td[contains(@class, 'titleColumn')]")

        for column in data_columns:
            link = column.xpath('./a')

            title = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()

            yield response.follow(
                    href,
                    callback=self.parse_story,
                    meta={ 'title': title }
        )

    def parse_story(self, response):
        summary = (
            response.xpath("//div[contains(@class, 'summary_text')]/text()")
            .extract_first()
            .strip()
        )

        loader = ItemLoader(item=MovieItem(), response=response)
        loader.add_value('title', response.meta.get('title'))
        loader.add_value('summary', summary)

        return loader.load_item()
