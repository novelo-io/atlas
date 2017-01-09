import scrapy


class Salary(scrapy.Item):

    sector = scrapy.Field()
    name = scrapy.Field()
    role = scrapy.Field()
    gross_salary = scrapy.Field()
    net_salary = scrapy.Field()
