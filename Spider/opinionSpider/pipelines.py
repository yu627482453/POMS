# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

from opinionSpider.opinionSpider.config.config import EConfig


class OpinionspiderPipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        path = EConfig.get_download_path()
        with open(path + "0.json", "a+") as f:
            line = json.dumps(ItemAdapter(item).asdict())
            f.write(line)
        return item
