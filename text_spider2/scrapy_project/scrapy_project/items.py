# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field 
class InformationItems(Item):
    _id=Field() 
    NickName=Field()
    Gender=Field()
    Province=Field()
    City=Field()
    Signature=Field()
    URL=Field()

class TweetsItem(Item):
    Content=Field()
    PubTime=Field()
    Co_oridinates=Field()
    