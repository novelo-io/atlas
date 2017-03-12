import scrapy


class Salary(scrapy.item.Item):

    sector = scrapy.Field()
    name = scrapy.Field()
    role = scrapy.Field()
    gross_salary = scrapy.Field()
    net_salary = scrapy.Field()
    as_of = scrapy.Field()
    link = scrapy.Field()
    download_time = scrapy.Field()
