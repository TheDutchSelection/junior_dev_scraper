import scrapy
import json
import re
from w3lib.url import add_or_replace_parameter

# See https://www.cars24.com/ae/buy-used-cars-dubai/


class Car24Spider(scrapy.Spider):
    name = 'cars24_com_spider'
    start_urls = ['https://www.cars24.com/ae/buy-used-cars-dubai/']

    def parse(self, response):
        for car in response.css('div._3IIl_ a._1Lu5u'):
            yield{
                'brand': car.css('.RZ4T7::text').get(),
                'engine_size': car.css('._3ZoHn li~ li+ li::text').get(),
                'year_of_manufacture' : car.css('._1i1E6::text').get(),
                'Deeplink': car.css(' a::attr(href) ').get(),
                'fuel_type': car.css('div.qeOgt::text').get(),
                'price': car.css('._7yds2::text').get(),
                'model': car.css('h3.RZ4T7::text').get(),
                'mileage': car.css('._3ZoHn li:nth-child(2)::text').get()
            }

            pass
