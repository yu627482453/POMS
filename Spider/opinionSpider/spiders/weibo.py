# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: weibo.py
@time1: 2021/4/22 10:59
"""
import datetime
import json
import re
import time
from abc import ABC
from bs4 import BeautifulSoup

import uuid
import scrapy

from opinionSpider.conf.weibo import WeiboConfig
from opinionSpider.items import OItem


class WeiboSpider(scrapy.Spider, ABC):
    name = 'weibo'

    def start_requests(self):
        yield scrapy.Request(WeiboConfig().get_hot(), callback=self.parse_hot)

    def parse_hot(self, response):
        hot_json = json.loads(response.text)
        if hot_json['ok'] != 1:
            return
        datas = hot_json['data']['statuses']
        for data in datas:
            oItem = OItem()
            try:
                oItem['id'] = str(uuid.uuid1())
            except KeyError:
                pass
            try:
                time1 = time.strptime(data['created_at'], "%a %b %d %H:%M:%S %z %Y")
                oItem['createdTime'] = time.strftime("%Y %M %d %H:%M:%S", time1)
            except KeyError:
                pass
            try:
                oItem['author'] = data['user']['screen_name']
            except KeyError:
                pass

            try:
                repost_count = data['reposts_count']
                comment_count = data['comments_count']
                attitude_count = data['attitudes_count']

                oItem['heat'] = int(repost_count) * 0.4 + int(comment_count) * 0.5 + int(attitude_count) * 0.01
            except KeyError:
                oItem['heat'] = 0

            oItem['selectTime'] = datetime.datetime.now().strftime("%Y %M %d %H:%M:%S")

            oItem['originId'] = uuid.uuid3(uuid.NAMESPACE_OID, oItem['text'])

            yield scrapy.Request(WeiboConfig().get_extend(data['id']), callback=self.parse_extend,
                                 meta={'oItem': oItem})

    def parse_extend(self, response):
        oItem: OItem = response.meta['oItem']
        extend_json = json.loads(response.text)
        if extend_json['ok'] != 1:
            return
        data = extend_json['data']
        oItem['text'] = BeautifulSoup(data['longTextContent']).get_text()

        match_obj = re.search(r"#(.*)#", oItem['text'])
        if match_obj:
            oItem['title'] = match_obj.group()
        else:
            oItem['title'] = ""

        yield oItem
