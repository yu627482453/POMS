# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import time

from itemadapter import ItemAdapter

from opinionSpider.conf.conf import EConfig


class OpinionspiderPipeline:

    def open_spider(self, spider):
        path = EConfig.get_download_path()
        if not spider.name == 'topfish':
            self.file = open(path + "/analyze.log", "a+")
        else:
            self.file = open(path + "/save.log", "a+")

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict())
        self.file.write(line + "\n")

    def close_spider(self, spider):
        self.file.close()
