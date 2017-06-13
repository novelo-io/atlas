import scrapy
from councilman.items import Councilman


class CouncilmanSpider(scrapy.Spider):

    name = 'councilman_spider'
    start_urls = [
        'http://www.camara.sp.gov.br/vereadores/',
        'http://www.camara.sp.gov.br/vereadores/?filtro=licenciados'
    ]

    def parse(self, response):
        councilmen = response.xpath("//article[@class='vereador-profile-thumb cf']")
        for item in councilmen:
            link_tag = item.css('.vereador-name > a')

            name = link_tag.css('a::text').extract_first()
            link = link_tag.css('a::attr(href)').extract_first()

            item = Councilman()
            item['name'] = name
            item['page_link'] = link

            yield scrapy.Request(link, meta={'item': item}, callback=self.parse_councilman)

    def parse_councilman(self, response):
        item = response.meta['item']

        party = response.xpath("//h3[@class='vereador-party']/img/@title").extract_first()
        picture = response.xpath("//h1[@class='vereador-picture']/a/img/@src").extract_first()

        info = response.xpath("//div[@class='vereador-data']/ul")

        phone_number = info.xpath("//li/strong[contains(text(),'Telefone')]/../text()").extract_first(default='')
        email = info.xpath("//li/strong[contains(text(),'E-mail')]/../a/text()").extract_first(default='')
        address = info.xpath(
            "//li/strong[contains(text(),'Endereço para correspondência')]/../text()"
        ).extract_first(default='')
        floor = info.xpath("//li/strong[contains(text(),'Andar')]/../text()").extract_first(default='')
        room = info.xpath("//li/strong[contains(text(),'Sala')]/../text()").extract_first(default='')

        biography = response.xpath("//section[@class='entry-content cf']/span/text()").extract_first(default='')

        item['phone_number'] = phone_number
        item['email'] = email
        item['address'] = address
        item['floor'] = floor
        item['room'] = room
        item['biography'] = biography

        item['party'] = party
        item['picture'] = picture
        item['status'] = 1

        return item
