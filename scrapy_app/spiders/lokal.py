from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy_app.items import LinkItem

class LokalSpider(BaseSpider):
    name = 'lokal'
    allowed_domains = ['http://localhost']
    start_urls = ['http://localhost/']

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//a')
        lynks =  []
        for l in links:
            i = LinkItem()
            i['page'] = response.url
            i['href'] = l.xpath('@href').extract()
            i['name'] = l.xpath('text()').extract()
            i['headers'] = {'type': response.headers['Content-Type'], 'status': response.status }
            lynks.append(i)
        
        return lynks
