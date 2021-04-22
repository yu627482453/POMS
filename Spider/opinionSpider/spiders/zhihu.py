# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: zhihu.py
@time1: 2021/4/22 21:19
"""
from abc import ABC

import scrapy


class ZhihuSpider(scrapy.Spider, ABC):

    def start_requests(self):
        pass
