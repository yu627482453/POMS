# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: weibo.py
@time1: 2021/4/22 10:53
"""
from opinionSpider.opinionSpider.config.config import EConfig


class WeiboConfig:

    def __init__(self):
        self._hot = "https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_8999_-_ctg1_8999_home"
        self._extend = "https://m.weibo.cn/statuses/extend?id={id}"

        self._top = "https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1" \
                    "%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=seat%3D1%26pos" \
                    "%3D0_0%26mi_cid%3D100103%26cate%3D10103%26filter_type%3Drealtimehot%26c_type%3D30%26display_time" \
                    "%3D1612419453&luicode=10000011&lfid=231583"

        self._hotword = "https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot" \
                        "%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=seat" \
                        "%3D1%26pos%3D0_0%26mi_cid%3D100103%26cate%3D10103%26filter_type%3Drealtimehot%26c_type%3D30" \
                        "%26display_time%3D1612419453&luicode=10000011&lfid=231583 "

    def get_hot(self):
        return self._hot

    def get_extend(self, id1):
        return self._extend.format(id=id1)

    def get_top(self):
        return self._top

    def get_hotword(self):
        return self._hotword

    def get_heat_model(self):
        return EConfig.get_spider_config()['weibo']['heat']
