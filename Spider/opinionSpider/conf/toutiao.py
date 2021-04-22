# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: toutiao.py
@time1: 2021/4/22 19:04
"""


class ToutiaoConfig:

    def __init__(self):

        self._hot_url = "https://www.toutiao.com/api/pc/feed/?"

    def get_hot_url(self):
        return self._hot_url
