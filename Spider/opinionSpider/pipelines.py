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
        self.dict1 = {
            "type": 0,
            "list": []
        }

    def process_item(self, item, spider):
        self.dict1["list"].append(ItemAdapter(item).asdict())

    def close_spider(self, spider):
        path = EConfig.get_download_path()
        time1 = time.gmtime()
        time2 = time.strftime("%m-%d", time1)
        with open(path + "/" + str(time2) + ".log", "a+") as f:
            line = json.dumps(self.dict1)
            f.write(line)

