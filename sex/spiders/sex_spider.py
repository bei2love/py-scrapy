from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from sex.items import SexItem

class SexSpider(CrawlSpider):
    name = 'sex'
    allowed_domains = ['sku117.pw']
    start_urls = ['http://d2.sku117.pw/pw/thread.php?fid=15']

    rules = (
        Rule(SgmlLinkExtractor(allow = ('/htm_data/15/1804/.*\.html')), callback = 'parse_page', follow = True),
    )

    def parse_page(self, response):
        def value(list):
            return list[0] if len(list) else ''


        item = SexItem()
        sel = Selector(response)
        item['title'] = value(sel.xpath('//h1[@id="subject_tpc"]/text()').extract()).encode("utf-8")
        item['url'] = response.url
        return  item