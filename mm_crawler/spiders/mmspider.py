# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import re
from items import ImageItem


class MmspiderSpider(CrawlSpider):
    name = 'mmspider'
    allowed_domains = ['22mm.cc']
    start_urls = ['http://www.22mm.cc/mm/qingliang/']
    rules = (
        Rule(
            LinkExtractor(
                allow=('index_\d+\.html', ), unique=True),
                 # restrict_xpaths=('//div[@class="ShowPage"]/a', 
                 #     '//div[@class="c_inner"]/ul[@class="pic"]/li/a')), 
            follow=True),
        Rule(
            LinkExtractor(
                allow=('\w+(\-\d+)?\.html', ), ),
                # restrict_xpaths=('//div[@class="pagelist"]/a/@href', )), 
            callback='image_link_getter',
            follow=True)
            )

    def image_link_getter(self, response):
        imageItem = ImageItem()
        pat = re.compile(r'arrayImg\[0\]="(.*?)";')
        ma = pat.search(response.body)
        if ma:
            imageItem['image_urls'] = (ma.group(1), )
            yield imageItem