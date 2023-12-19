import scrapy
from pathlib import Path

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml",]

    def parse(self, response):
        filename = "teacher.html"
        Path(filename).write_bytes(response.body)
