__author__ = 'Asus'
import scrapy
from scrapy.http import Request

class TcUrlSpider(scrapy.Spider):
    name = "tcurl"
    allowed_domains = ["techcrunch.com"]
    start_urls = [
        "http://techcrunch.com/gadgets/page/458"
    ]

    def parse(self, response):
        filename = "urls.txt"
        f=open(filename,'a')
        print response.url
        for art in response.xpath('//h2[@class="post-title"]'):
            #title = art.xpath('a/span/text()').extract()
            link = art.xpath('a/@href').extract()
            #desc = art.xpath('text()').extract()
            if(len(link)>0):
                try:
                    f.write(link[0]+"\n")
                except:
                    print "file write except"
        nextPage = response.xpath('//div[@class="pagination-container"]//li[@class="next"]/a/@href').extract()
        if len(nextPage)>0:
            print "http://techcrunch.com"+nextPage[0]
            request=Request("http://techcrunch.com"+nextPage[0])
            yield request
        return