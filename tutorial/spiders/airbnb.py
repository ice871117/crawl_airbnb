# -*- coding: utf-8 -*-
import scrapy


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['airbnb.com']
    start_urls = ['https://www.airbnb.com/s/Shanghai--China/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&query=Shanghai%2C%20China&place_id=ChIJMzz1sUBwsjURoWTDI5QSlQI&checkin=2020-04-29&checkout=2020-05-01&adults=2&source=structured_search_input_header&search_type=search_query']

    def parse(self, response):
        firstRoom = response.xpath('//*[@id="ExploreLayoutController"]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div')
        content = firstRoom.xpath('./meta[1]/@content').extract()
        position = firstRoom.xpath('./meta[2]/@content').extract()
        url = firstRoom.xpath('./meta[3]/@content').extract()
        print(content)
        print("\n")
        print(position)
        print("\n")
        print(url)
        print("\n")
