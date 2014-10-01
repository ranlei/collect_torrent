# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import subprocess
import time
import urllib2
from scrapy.http.request import Request

class TorrentPipeline(object):
    def process_item(self,  item,  spider):
        print 'Downloading ' + item['title'][0]
        path = item['torrent'][0]
        print path
        subprocess.call(['./curl_torrent.sh',path])
        time.sleep(10)
        return item
