import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class VedbotSpider(CrawlSpider):
    name = 'vedbot'
    allowed_domains = None
    start_urls = None
    crawl_count = 0
    max_url_value = 1000
    failed_url = []
    rules = [Rule(LxmlLinkExtractor(allow=()), callback="parse_item", follow=True)]

    def __init__(self, start_url, allowed_domains=None):
        self.start_urls = [start_url]
        if allowed_domains is None:
            self.allowed_domains = [start_url.split("www.")[1].split(".")[0]]
        else:
            self.allowed_domains=[allowed_domains]
        print("Start_url={}, Allowed_domain={}".format(self.allowed_domains, self.start_urls))

    # # Method which starts the requests by visiting all URLs specified in start_urls
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.parse, dont_filter=True)

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
                    from_title = response.xpath("//title/text()").extract()
                    clean_data = response.xpath("(//div | //p | //a )/text()").extract()
                    items.append(
                        {"Url_from": response.url, "Url_to": link.url, "title": from_title, "dump": response.text,
                         "clean_data": clean_data})
        return items
