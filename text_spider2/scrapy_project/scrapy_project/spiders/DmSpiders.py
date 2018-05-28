# encoding=utf-8


import re
import datetime
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy_project.items import InformationItems,TweetsItem
Header = {
    "Host":
    "my.sina.com.cn",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":
    "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":
    "gzip, deflate",
    "Connection":
    "keep-alive",
    
}



class Spider1(CrawlSpider):
    name = "sinaSpider1"
    host = "http://weibo.cn"
    start_urls = [
        13968760795
    ]
    scrawl_ID = set(start_urls)  # 记录待爬的微博ID
    finish_ID = set() # 记录已爬的微博ID
    def start_requests(self):
        while self.scrawl_ID.__len__():
            ID = self.scrawl_ID.pop()
            self.finish_ID.add(ID)  # 加入已爬队列
            ID = str(ID)
            url_information0 = "https://weibo.cn/%s/info" % ID
            url_tweets = "http://weibo.cn/%s/profile?filter=1&page=1" % ID
            yield Request(url=url_tweets,headers=Header, meta={"ID": ID}, callback=self.parse1)
            yield Request(url=url_information0,headers=Header, meta={"ID": ID}, callback=self.parse0) 

    def parse1(self, response):
        selector = Selector(response)
        tweets = selector.xpath('body/div[@class="c" and @id]')
        for tweet in tweets:
            tweetsItems = TweetsItem()
            id = tweet.xpath('@id').extract_first()  
            content = tweet.xpath('div/span[@class="ctt"]/text()').extract_first()  
            cooridinates = tweet.xpath('div/a/@href').extract_first()  
    
            tweetsItems["ID"] = response.meta["ID"]
            tweetsItems["_id"] = response.meta["ID"] + "-" + id
            if content:
                tweetsItems["Content"] = content.strip(u"[\u4f4d\u7f6e]")  
            if cooridinates:
                cooridinates = re.findall('center=([\d|.|,]+)', cooridinates)
                if cooridinates:
                    tweetsItems["Co_oridinates"] = cooridinates[0]
            yield tweetsItems
    def parse0(self, response):
        informationItems = InformationItems()
        selector = Selector(response)
        text1 = ";".join(selector.xpath('body/div[@class="c"]/text()').extract())  
        nickname = re.findall(u'\u6635\u79f0[:|\uff1a](.*?);', text1)  
        gender = re.findall(u'\u6027\u522b[:|\uff1a](.*?);', text1) 
        place = re.findall(u'\u5730\u533a[:|\uff1a](.*?);', text1)  
        signature = re.findall(u'\u7b80\u4ecb[:|\uff1a](.*?);', text1) 
        url = re.findall(u'\u4e92\u8054\u7f51[:|\uff1a](.*?);', text1)  
        if nickname:
            InformationItems["NickName"] = nickname[0]
        if gender:
            informationItems["Gender"] = gender[0]
        if place:
            place = place[0].split(" ")
            informationItems["Province"] = place[0]
            if len(place) > 1:
                informationItems["City"] = place[1]
        if signature:
            informationItems["Signature"] = signature[0]
        if url:
            informationItems["URL"] = url[0]
        print informationItems
        yield informationItems
             
