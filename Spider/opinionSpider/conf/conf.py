# -*- coding:utf-8 -*-
"""
@project：Spider
@author: Nero
@file: conf.py
@time1: 2021/4/22 10:21
"""
import os
import yaml


class EConfig:

    @staticmethod
    def _get_conf_path():

        conf_re_path = "/../conf/"
        conf_abs_path = os.path.abspath(os.path.curdir + conf_re_path)
        return conf_abs_path

    @staticmethod
    def get_download_path():
        download_re_path = "/../logs/"
        download_abs_path = os.path.abspath(os.path.curdir + download_re_path)
        return download_abs_path

    @staticmethod
    def get_spider_config():
        conf_abs_path = EConfig._get_conf_path()
        spider_config = conf_abs_path + "/spider.yaml"
        file = open(spider_config)
        data_dict = yaml.load(file)
        file.close()
        return data_dict

    @staticmethod
    def get_main_config():
        conf_abs_path = EConfig._get_conf_path()
        main_config = conf_abs_path + "/main.yaml"
        # TODO main_config
