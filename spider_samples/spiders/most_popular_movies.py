# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from spider_samples.items import MovieItem
from scrapy import Spider


class MostPopularMoviesSpider(Spider):
    name = 'most_popular_movies'
    start_urls = ['https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular']

    def parse(self, response):
        links = response.css('.discovery-tiles__wrap').xpath(".//a")

        for link in links:
            title = link.xpath(".//span/text()").get().strip()
            href = link.xpath('./@href').get()
            print(href)

            yield response.follow(
                href,
                callback=self.parse_movie,
                meta={'title': title}
            )

        tbody = response.xpath("//tbody[contains(@class, 'lister-list')]")
        data_columns = tbody.xpath("//td[contains(@class, 'titleColumn')]")

    def parse_movie(self, response):
        media_info = response.xpath("//section[contains(@class, media-info)]")

        summary = media_info.xpath(".//rt-text[contains(@data-qa, 'synopsis-value')]/text()").get()
        director = media_info.xpath(".//rt-link[contains(@data-qa, 'item-value')]/text()").get()

        loader = ItemLoader(item=MovieItem(), response=response)
        loader.add_value('title', response.meta.get('title'))
        loader.add_value('summary', summary)
        loader.add_value('director', director)

        return loader.load_item()
