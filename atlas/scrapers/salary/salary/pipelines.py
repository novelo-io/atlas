import datetime
from scrapy import signals
from scrapy.exporters import CsvItemExporter


class SalaryPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        today = datetime.date.today()
        file = open(f'../../data/{today}-salary.csv', 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        if isinstance(item['name'], str):
            item['name'] = item['name'].strip()
        if isinstance(item['role'], str):
            item['role'] = item['role'].strip()

        self.exporter.export_item(item)
        return item
