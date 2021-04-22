# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: topfish.py
@time1: 2021/4/22 22:14
"""
import json
import uuid
import time

import scrapy
import requests

from abc import ABC

from opinionSpider.items import OItem
from opinionSpider.conf.topfish import TopfishConfig


class TopfishSpider(scrapy.Spider, ABC):
    name = 'topfish'

    def start_requests(self):
        yield scrapy.Request(url=TopfishConfig().get_all_type(), callback=self.parse_type)

    def parse_type(self, response):
        json_type = json.loads(response.text)

        datas = json_type['Data']['综合']

        for data in datas:
            yield scrapy.Request(url=TopfishConfig().get_index().format(id=data['id']), callback=self.parse_index,
                                 meta={'source': data['name']})

    def parse_index(self, response):
        json_index = json.loads(response.text)
        datas = json_index['Data']['data']

        oItem = OItem()
        for data in datas:
            try:
                oItem['id'] = str(uuid.uuid1())
            except KeyError:
                pass
            try:
                oItem['title'] = data['Title']
            except KeyError:
                pass
            try:
                oItem['text'] = data['text']
            except KeyError:
                pass
            try:
                oItem['url'] = self.parse_url(data['Url'])
                print(oItem['url'])
            except KeyError:
                pass
            try:
                oItem['source'] = response.meta['source']
            except KeyError:
                oItem['source'] = ""

            try:
                time1 = time.localtime(data['CreateTime'])
                oItem['createdTime'] = time.strftime("%Y %M %d %H:%M:%S", time1)
            except KeyError:
                pass
            yield oItem

    def parse_url(self, url):
        header = {
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
            "Sec-Fetch-Dest": "document",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Referer": "https://mo.fish/?class_id=%E5%85%A8%E9%83%A8&hot_id=1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
        }
        res = requests.get(url, headers=header, allow_redirects=False)
        return res.headers["location"]
