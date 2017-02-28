
BOT_NAME = 'salary_scraper'

SPIDER_MODULES = ['salary.spiders.spider']
NEWSPIDER_MODULE = 'salary.spiders'

LOG_ENABLED = True

ITEM_PIPELINES = {
    'salary.pipelines.SalaryPipeline': 300,
}
