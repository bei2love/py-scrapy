from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from sex.items import SexItem

class SexSpider(CrawlSpider):
    name = 'sex'
    allowed_domains = ['sku117.pw']
    start_urls = ['http://d2.sku117.pw/pw/thread.php?fid=15']

    rules = {
        # Rule(LinkExtractor(allow=('/thread\.php\?fid=15\&page=\d+'), restrict_xpaths="//div[@class='pages']"), follow=True),
        Rule(LinkExtractor(allow=('/htm_data/15/1804/.*\.html'), restrict_xpaths="//table[@id='ajaxtable']"), callback='parse_item')
    }


    def parse_item(self, response):

        def value(list):
            return list[0] if len(list) else ''
        print(response.url)

        item = SexItem()

        if response.status == 200:
            try:
                item['title'] = value(response.xpath('//h1[@id="subject_tpc"]/text()').extract()).encode("utf-8")
                item['url'] = response.url

                list_imgs = response.xpath('//div[@class="tpc_content"]//img/@src').extract()
                # print("--------------------------------- img list begin ----------------------------------")
                # print(type(list_imgs))
                # print(list_imgs)
                # print("--------------------------------- img list end ----------------------------------")
                if list_imgs:
                    item['image_urls'] = self.url_join(list_imgs, response)
                yield item
            except:
                print("--------------------------------- error ----------------------------------")

        else:
            print("**********************************************")

    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls

