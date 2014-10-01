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
        xp = lambda x,y: x.xpath(y).extract()
        entires = response.xpath('//tr[starts-with(@id,"torrent_")]')
        items = []
        for entry in entires:
            print entry
            item = TorrentItem()
            item['title'] = xp(entry,'td[1]/div[2]/div[1]/a[1]/text()')
            item['url'] = xp(entry,'td[1]/div[2]/div[1]/a[1]/@href')
            item['torrent'] = xp(entry,'td[1]/div[1]/a[starts-with(@title,"Download torrent file")]/@href')
            item['size'] = xp(entry,'td[2]/text()')
            item['sizeType'] = xp(entry,'td[2]/span/text()')
            item['age'] = xp(entry,'td[4]/text()')
            item['seed'] = xp(entry,'td[5]/text()')
            item['leech'] = xp(entry,'td[6]/text()')
            # for s in self.keywords:
                # if s.lower() in item['title'][0].lower():
            items.append(item)
                    # break
        return items