import scrapy


class Councilman(scrapy.Item):

    name = scrapy.Field()
    page_link = scrapy.Field()
    phone_number = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    floor = scrapy.Field()
    room = scrapy.Field()
    biography = scrapy.Field()
    party = scrapy.Field()
    picture = scrapy.Field()
