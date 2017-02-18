import scrapy
from councilman.items import Councilman


class CouncilmanSpider(scrapy.Spider):

    name = 'councilman_spider'
    start_urls = ['http://www.camara.sp.gov.br/vereadores/']

    def parse(self, response):
        councilmen = response.xpath("//article[@class='vereador-profile-thumb cf']")
        for item in councilmen:
            link_tag = item.css('.vereador-name > a')

            name = link_tag.css('a::text').extract_first()
            link = link_tag.css('a::attr(href)').extract_first()

            item = Councilman()
            item['name'] = name
            item['page_link'] = link

            print(name)
            print(link)

            yield scrapy.Request(link, meta={'item': item}, callback=self.parse_councilman)

    def parse_councilman(self, response):
        item = response.meta['item']

        info = response.xpath("//div[@class='vereador-data']/ul")

        phone_number = info.xpath("//li/strong[contains(text(),'Telefone')]/../text()").extract_first(default='').strip()
        email = info.xpath("//li/strong[contains(text(),'E-mail')]/../a/text()").extract_first(default='').strip()
        address = info.xpath(
            "//li/strong[contains(text(),'Endereço para correspondência')]/../text()"
        ).extract_first(default='').strip()
        floor = info.xpath("//li/strong[contains(text(),'Andar')]/../text()").extract_first(default='').strip()
        room = info.xpath("//li/strong[contains(text(),'Sala')]/../text()").extract_first(default='').strip()

        biography = response.xpath("//section[@class='entry-content cf']/span/text()").extract_first()

        item['phone_number'] = phone_number
        item['email'] = email
        item['address'] = address
        item['floor'] = floor
        item['room'] = room
        item['biography'] = biography

        return item
