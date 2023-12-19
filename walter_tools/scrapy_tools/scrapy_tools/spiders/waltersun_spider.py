import scrapy
from pathlib import Path

class WaltersunSpiderSpider(scrapy.Spider):
    name = "waltersun_spider"
    allowed_domains = ["waltersun.cn"]
    start_urls = ["https://www.waltersun.cn/zh/documents/"]

    def parse(self, response):
        filename = "waltersun.html"
        Path(filename).write_bytes(response.body)
