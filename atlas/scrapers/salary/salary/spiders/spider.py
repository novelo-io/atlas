import datetime
import scrapy
from salary.items import Salary


class SalarySpider(scrapy.Spider):

    name = 'salary_spider'
    base_url = 'http://www2.camara.sp.gov.br/SalariosAbertos/HTML_ativos_2017_01'
    start_urls = [
        f'{base_url}/todos.html'
    ]

    def parse(self, response):
        sector = None

        now = datetime.datetime.now()

        for i, row in enumerate(response.xpath("//table[@id='tabela_principal']//tr")):
            text_sector = row.css(".lin_lotacao::text").extract_first()

            if text_sector is not None:
                sector = text_sector.strip()

            name = row.css(".nome_valor::text").extract_first()

            if name is not None:

                hidden_name = row.css(".nome_valor span::text").extract_first()
                if hidden_name is not None:
                    name = hidden_name

                role = row.css(".cargo_valor::text").extract_first()
                salary = row.css(".remun_valor")
                salary_link = salary.css("a::attr(href)").extract_first()
                salary_url = "{0}/{1}".format(self.base_url, salary_link)

                item = Salary()
                item['sector'] = sector
                item['name'] = name
                item['role'] = role
                item['link'] = salary_url
                item['download_time'] = now

                yield scrapy.Request(salary_url, meta={'item': item}, callback=self.parse_salary)

    def parse_salary(self, response):
        item = response.meta['item']

        gross_salary = response.xpath(
            u"//table[@id='tbl_detalhes']//tr//td[contains(text(),'Remuneração bruta do mês')]/../td[@class='moeda']/text()"
        ).extract_first()
        net_salary = response.xpath(
            u"//table[@id='tbl_detalhes']//tr//td[contains(text(),'Remuneração líquida')]/../td[@class='moeda']/text()"
        ).extract_first()

        item['gross_salary'] = gross_salary
        item['net_salary'] = net_salary

        yield item
