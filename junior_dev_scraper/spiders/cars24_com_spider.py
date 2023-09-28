import scrapy
import json
import re
import benedict
from w3lib.url import add_or_replace_parameter

# See https://www.cars24.com/ae/buy-used-cars-dubai/


class Car24ComSpider(scrapy.Spider):
    name = 'cars24_com_spider'

    # Good luck
    start_urls = [
        "https://www.cars24.com/ae/buy-used-cars-dubai/",
    ]
    custom_settings = {
        'FEEDS': { 'Output.csv': { 'format': 'csv',}}
    }
    def parse(self, response):
        for cars in response.css("div._3IIl_._1xLfH"):
            year =cars.css("p._1i1E6 ::text").get()[:4]
            fuel=cars.css("img._3oX3Z ::attr(alt)").get().split(',')[-1][:-4]
            yield {
                "Model": cars.css("h3.RZ4T7 ::text").get(),
                "DeepUrl": cars.css("div._3IIl_._1xLfH a._1Lu5u ::attr(href)").get(),
                "Price": cars.css("span._7yds2 ::text").get(),
                "Engine size": cars.css("ul._3ZoHn li::text")[2].get(),
                "Mileage": cars.css("ul._3ZoHn li::text")[1].get(),
                "Fuel": fuel,
                "Year": year,
            }
