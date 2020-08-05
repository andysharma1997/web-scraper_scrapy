import scrapy
from scrapy.spiders import CrawlSpider, Rule
# from vedantu_scraper.items import VedantuScraperItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import selenium
import requests
from lxml import etree
import json


# from scraper_api import ScraperAPIClient

# client = ScraperAPIClient('b354a392d75a2e5f362f21820a11e306')


# class VedbotSpider(scrapy.Spider):
#     name = 'vedbot'
#     allowed_domains = ['www.whitehatjr.com']
#     start_urls = ['https://www.whitehatjr.com/']
#
#     def parse(self, response):
#         print("Parsing {} page".format(response.url))
#         text_data = response.xpath("//p//text()").extract()
#         yield {
#             "text": text_data,
#             "link": response.url
#         }
#
#         NEXT_PAGE_SELECTOR = 'a ::attr(href)'
#         next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#         if requests.get(response.urljoin(next_page)).status_code == 200:
#             yield scrapy.Request(
#                 response.urljoin(next_page),
#                 callback=self.parse
#             )

class VedbotSpider(CrawlSpider):
    name = 'vedbot'
    allowed_domains = ['www.whitehatjr.com']
    start_urls = ['https://www.whitehatjr.com/']
    crawl_count = 0
    max_url_value = 1000
    failed_url = []
    rules = [Rule(LxmlLinkExtractor(allow=()), callback="parse_item", follow=True)]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_item(self, response):
        self.crawl_count += 1
        print("!!!!!!!!!!!!!!!!!!!")
        print("Parsing {} page, Crawl_Count={}".format(response.url, self.crawl_count))
        all_links = LxmlLinkExtractor(allow=(), unique=True, canonicalize=True).extract_links(response)
        items = []
        for link in all_links:
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
                if is_allowed:
                    try:
                        title = link

                    items.append({"Url_from": response.url, "Url_to": link.url,"title":})
        return items
        # return {
        #     "url": response.url,
        #     "page_links": [link.url for link in all_links]
        # }

        # text_data = response.xpath("//p//text()").extract()
        # yield {
        #     "text": text_data,
        #     "link": response.url,
        #     "complete_dump": response.text
        # }
        # NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page is not None:
        #     yield scrapy.Request(client.scrapyGet(url=response.urljoin(next_page), render=True), self.parse)

    # def handle_error(self, failure):
    #     url = failure.request.url
    #     print('Failure type: %s, URL: %s', failure.type, url)
    #     self.failed_url.append(url)
