# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: toutiao.py
@time1: 2021/4/22 19:38
"""
import datetime
import json
import time
import uuid
from abc import ABC

import scrapy

from opinionSpider.conf.toutiao import ToutiaoConfig
from opinionSpider.items import OItem


class ToutiaoSpider(scrapy.Spider, ABC):
    name = "toutiao"

    def start_requests(self):
        yield scrapy.Request(ToutiaoConfig().get_hot_url(), callback=self.parse_hot)

    def parse_hot(self, response):
        hot_json = json.loads(response.text)
        datas = hot_json['data']
        for data in datas:

            oItem: OItem = OItem()
            try:
                oItem['id'] = str(uuid.uuid1())
            except KeyError:
                pass
            try:
                oItem['title'] = data['title']
            except KeyError:
                pass
            try:
                oItem['text'] = data['abstract']
            except KeyError:
                pass
            try:
                time1 = time.localtime(data['behot_time'])
                oItem['createdTime'] = time.strftime("%Y %M %d %H:%M:%S", time1)
            except KeyError:
                pass
            try:
                oItem['author'] = data['source']
            except KeyError:
                pass
            try:
                repost_count = data['reportCount']
                comment_count = data['commentCount']
                attitude_count = data['attitudes_count']
                oItem['heat'] = int(repost_count) * 0.4 + int(comment_count) * 0.5 + int(attitude_count) * 0.01
            except KeyError:
                oItem['heat'] = 0

            oItem['selectTime'] = datetime.datetime.now().strftime("%Y %M %d %H:%M:%S")

            oItem['originId'] = uuid.uuid3(uuid.NAMESPACE_DNS, oItem['text'])

            yield oItem
