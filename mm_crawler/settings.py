# -*- coding: utf-8 -*-

# Scrapy settings for mm_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mm_crawler'

SPIDER_MODULES = ['mm_crawler.spiders']
NEWSPIDER_MODULE = 'mm_crawler.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = 'pics'
DOWNLOAD_DELAY = 0.1
CONCURRENT_REQUESTS = 1
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mm_crawler (+http://www.yourdomain.com)'
