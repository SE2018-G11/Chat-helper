# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


# encoding=utf-8
import random
from cookies import ck
from user_agent import agents
Proxy = [
    '180.122.155.55:31104',
]

class UserAgentMiddleware(object):
    """ ��User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ ��Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(ck)
        request.cookies = cookie
class Proxy_And_UsrAgent(object):
    
    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent',random.choice(agents))
        request.meta['proxy'] = 'http://' + random.choice(Proxy)