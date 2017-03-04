
class SalaryPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item['name'], str):
            item['name'] = item['name'].strip()
        if isinstance(item['role'], str):
            item['role'] = item['role'].strip()

        return item
