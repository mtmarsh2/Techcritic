from __future__ import absolute_import
import scrapy
from Scrapy.Scrapy.items import tcItem

class TcTextSpider(scrapy.Spider):
    name = "tctext"
    allowed_domains = ["techcrunch.com"]
    urlFile=open("urls.txt")
    lines=urlFile.readlines()

    start_urls = lines[0:1]

    def parse(self, response):
        # item=scrapy.tcItem()
        # item['url']=response.url
        # item['siteName']="Techcrunch"
        # item['title']=response.xpath('//h1[@class="alpha tweet-title"]/text()').extract()
        # print response.url, item['title']
        text=""
        for p in response.xpath('//div[@class="article-entry text"]/p'):
            p_text= p.xpath('text()').extract()
            print p_text
            if len(p_text)>0:
                text+=p_text[0]
        print text

        return