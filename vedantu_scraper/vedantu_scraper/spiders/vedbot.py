import scrapy
import requests


# class VedbotSpider(scrapy.Spider):
#     name = 'vedbot'
#     # allowed_domains = ['www.reddit.com/r/gameofthrones/']
#     start_urls = ['https://www.vedantu.com/']
#
#     def parse(self, response):
#         # Extracting the content using css selectors
#         print("Processing","--->",response.url)
#         text_data = response.xpath("//p//text()").extract()
#         a_selector = response.xpath("//a")
#         links=[]
#         for selectore in a_selector:
#             links.append(selectore.xpath("@href").extract_first())
#         # links = response.css("a::attr(href)").extract
#         print("Got links:{}".format(links))
#         # a_selector = response.xpath("//a")
#         # for selectore in a_selector:
#         #     text = selectore.xpath("text()").extract_first()
#         #     link = selectore.xpath("@href").extract_first()
#         #     request = response.follow(link, callback=self.parse)
#         #     yield request
#         try:
#             for link in links:
#                 yield {
#                     "text": text_data,
#                     "link": link
#                 }
#             # if 'vedantu' in link:
#             #     yield scrapy.Request(url=link, callback=self.parse)
#         except  TypeError:
#             pass

class VedbotSpider(scrapy.Spider):
    name = 'vedbot'
    # allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['https://www.whitehatjr.com/']

    def parse(self, response):
        print("Parsing {} page".format(response.url))
        text_data = response.xpath("//p//text()").extract()
        yield {
            "text": text_data,
            "link": response.url
        }
        # links = response.xpath("//a//@href").extract()
        # for link in links:
        #     yield

        NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if requests.get(response.urljoin(next_page)).status_code == 200:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
