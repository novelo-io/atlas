BOT_NAME = 'councilman_scraper'

SPIDER_MODULES = ['councilman.spiders.spider']
NEWSPIDER_MODULE = 'councilman.spiders'

LOG_ENABLED = True

ITEM_PIPELINES = {
    'councilman.pipelines.CouncilmanPipeline': 300,
}
