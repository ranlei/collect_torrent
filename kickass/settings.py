# -*- coding: utf-8 -*-

# Scrapy settings for collectTorrent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kickass'

SPIDER_MODULES = ['kickass.spiders']
NEWSPIDER_MODULE = 'kickass.spiders'
ITEM_PIPELINES = {'kickass.pipelines.TorrentPipeline':1,}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kickass (+http://www.yourdomain.com)'
# Download and traffic settings.
# Limit concurrent requests and add a 
# download delay to minimize hammering.
USER_AGENT = 'http://www.kickasstorrents.com'
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = False
CONCURRENT_REQUESTS_PER_DOMAIN = 1 #  Default: 8
#SCHEDULER = 'scrapy.core.scheduler.Scheduler'

# Log Settings
# LOG_ENABLED = True
# LOG_LEVEL = 'INFO' # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
# LOG_FILE = './kickass.log'
