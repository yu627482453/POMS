# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: zhihu.py
@time1: 2021/4/22 20:54
"""



class ZhihuConfig:

    def __init__(self):
        self._question_url = "https://www.zhihu.com/api/v4/questions/{qid}/answers?limit=20"

    def get_question_url(self):
        return self._question_url
