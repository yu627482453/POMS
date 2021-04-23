# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: topfish.py
@time1: 2021/4/22 21:42
"""


class TopfishConfig:
    def __init__(self):
        self._allType = "https://api.tophub.fun/GetAllType"
        self._index = "https://api.tophub.fun/v2/GetAllInfoGzip?id={id}&page=0"
        self._type = ["1065", "1", "58", "1053", "148", "1033"]

    def get_all_type(self):
        return self._allType

    def get_index(self):
        return self._index

    def get_type(self):
        return self._type
