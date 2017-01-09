import scrapy
from items import Salary


class SalarySpider(scrapy.Spider):

    name = 'salary_spider'
    base_url = 'http://www2.camara.sp.gov.br/SalariosAbertos/HTML_ativos_2016_11'
    start_urls = [
        '{0}/todos.html'.format(base_url)
    ]

    def parse(self, response):
        sector = None
        for i, item in enumerate(response.xpath("//table[@id='tabela_principal']//tr")):
            text_sector = item.css(".lin_lotacao::text").extract_first()
            if text_sector is not None:
                sector = text_sector.strip()

            name = item.css(".nome_valor::text").extract_first()

            if name is not None:
                name = name.strip()
                role = item.css(".cargo_valor::text").extract_first()
                salary = item.css(".remun_valor")
                salary_link = salary.css("a::attr(href)").extract_first()
                salary_link = "{0}/{1}".format(self.base_url, salary_link)

                role = role.strip()

                item = Salary()
                item['sector'] = sector
                item['name'] = name
                item['role'] = role

                yield scrapy.Request(salary_link, meta={'item': item}, callback=self.parse_salary)

    def parse_salary(self, response):
        item = response.meta['item']

        gross_salary = response.xpath(
            "//table[@id='tbl_detalhes']//tr//td[contains(text(),'Remuneração bruta do mês')]/../td[@class='moeda']/text()"
        ).extract_first()
        net_salary = response.xpath(
            "//table[@id='tbl_detalhes']//tr//td[contains(text(),'Remuneração líquida')]/../td[@class='moeda']/text()"
        ).extract_first()

        item['gross_salary'] = gross_salary
        item['net_salary'] = net_salary

        yield item
