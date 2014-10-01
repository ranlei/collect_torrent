from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from kickass.items import TorrentItem
class KickassSpider(Spider):
    name = "kickass"
    allowed_domains = [
         "kat.ph"
    ]
    def __init__ (self,  *args,  **kwargs):
        super(KickassSpider,self).__init__(*args, **kwargs)
        self.keywords = kwargs['keywords'].split(',')
        self.category = kwargs['category']
        self.start_urls = [
            'http://kat.ph/usearch/category%3A'
            +self.category+'/?field=time_add&sorder=desc'
        ]

    def parse(self,  response):

        entires = response.xpath('//div[@class="markeredBlock torType pdfType"]/a')
        items = [ ]
        for entry in entires:
            item = TorrentItem()
            print entry
            # item['title'] = entry.xpath('td[1]/div[2]/a[2]/text()').extract()
            # item['url'] = entry.xpath('td[1]/div[2]/a[2]/@href').extract()
            item['torrent'] = entry.xpath('attribute::href').extract()
            print item['torrent']
            item['size'] = entry.xpath('child::text()').extract()
            print item['size']
            item['sizeType'] = entry.xpath('td[2]/span/text()').extract()
            item['age'] = entry.xpath('td[4]/text()').extract()
            item['seed'] = entry.xpath('td[5]/text()').extract()
            item['leech'] = entry.xpath('td[6]/text()').extract()
            # for s in self.keywords:
            #     if s.lower() in item['title'][0].lower():
            #         items.append(item)
            #         break
        return items