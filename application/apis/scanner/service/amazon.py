import re
from application.core.db.models.scan import PLATFORM, ITEM
from application.core.scanner.site_scanner import SitesScrape
from application.core.db_logic.amazon import store_amazon_data, get_scan_item


def run_amazon_scanner(search_item, page):
    amazon = SitesScrape()
    data = amazon.get_amazon_bulk_data(page, search_item)
    
    parse_data = parse_amazon_data(data)
    final_data = prepare_data(parse_data)
    store_amazon_data(final_data)
    return "data has been stored"

def parse_amazon_data(data):
    print(data.keys())
    _temp = []
    for value in data.keys():
        for row in data[value]:
            _temp.append(row)
    print(len(_temp))
    return _temp

def prepare_data(data):
    for point in range(0, len(data)):

        if data[point]['price']: 
            if ',' in data[point]['price']: 
                data[point]['price'] = int(data[point]['price'].replace(',','').replace('.',''))
        if data[point]['star']:
            star_value = re.findall(r"[-+]?\d*\.\d+|\d+", data[point]['star'])
            if star_value:
                star_value = star_value[0]
                data[point]['star'] = float(star_value)
        if data[point]['rating']:
            data[point]['rating'] = int(data[point]['rating'].replace(',',''))
        data[point]['platform'] = PLATFORM.AMAZON
        data[point]['item'] = ITEM.MOBILE

    return data

