

class CouncilmanPipeline(object):

    def process_item(self, item, spider):
        item['name'] = item['name'].strip()
        item['address'] = item['address'].strip()
        item['biography'] = item['biography'].strip()
        item['floor'] = item['floor'].strip()
        item['room'] = item['room'].strip()
        return item
