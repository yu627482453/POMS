# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: toutiao.py
@time1: 2021/4/22 19:38
"""
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
                reportCount = data['reportCount']
            except KeyError:
                pass
            try:
                commentCount = data['commentCount']
            except KeyError:
                pass
            try:
                attitudeCount = data['attitudes_count']
            except KeyError:
                pass
            # TODO heat

            yield oItem
