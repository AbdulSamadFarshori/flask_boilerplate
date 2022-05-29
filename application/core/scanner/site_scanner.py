import requests
from bs4 import BeautifulSoup
import time

class SitesScrape(object):

    def url_template(self, search_item, page):
        s_word = search_item.replace(" ", "+")
        url = "https://www.amazon.in/s?k={}&page={}".format(s_word, page)
        return url

    
    def get_html_content(self, search_item, page):
        cookies = { 'ubid-acbin' : '260-9123249-4730752', 'lc-acbin':'en_IN', 'x-acbin':'TB4HUF?kaSP8AFScWDD04VyVForpUpQJs3cOfQ?JE2UUVSbPK9bDvEcKryQElVuZ',
                    'at-acbin' : 'Atza|IwEBIPVNul7h39LiZ955lKYmLa3JOwWy4Z6ZQTpuJRpdPRz_QyEF7phhhJDuprLahT09VrlJWMJHhOY61RCLvbbh7fvSQrDgxggKu-howJIXSWY8xAGARW_dBj6V6MUb1angfML5RFC_6WTZLZ7SlYWHXsGvFyHZZT4vd0rZKiVBAjzD9pLn3509qAhNRWEYrLwMQ1bufvPsPMmVrdLfaqyKGv3l', 
                    'sess-at-acbin' : '5ALP5/+RXCfLYlci1CqUMOZVW3TxRzG9wjG0gjJA4Pw=', 'sst-acbin':'Sst1|PQHb9w_2pGPNFHWl2kPj793ZCfjlW1Xtx9HRymI-a9s6ogg2Ad0bLs19aEjwjGzJhID7LNjU2_9tnSgPm9vtXOG68GgSnH6gdiRD2S0R3QvOM3iHuPVz-f-74tKN5kF-aW4elEi2ZkhcSdG8eM7uCD4oyfdLGsvMu-m3Si1UT4vgl_QWCKgrsokxsiKjZugVEppulE25eh_eIMOe1ORZKsoBUchzMv_zJPShn2fkzKVFsEtCQzlnRor4HJgOfgPNcFVVqzj80tjFjRITbzUNA2MV31kq0UGCxaumVAsAOU4zldw', 
                    'i18n-prefs':'INR', 'session-id':'260-0869841-2655858', 
                    'csm-hit' : 'tb:s-4BPWC04MVX04Y8K54GZ0|1653809502965&t:1653809503393&adb:adblk_yes; session-token=9c2FoeGUbFMpkRG20HToUwg3IROdXS04Ju0OORHOjanV8tz1yahPJCce6yLdc1mI5w9+dN/cNHzwl37hOIo9fp1m/UhjdYZse4wZ8t4lZ80ngkY3pErQtGNjWEFKuSVWXOq/tdCkXgF9JUE/pLCbzkoo9SHX9KVEoeZ9g1mH0DaR31NxSPU9klsdvqZiqCGtoic76hFT7diaOwjoKqJ4auxOxSAx8YXF',
                    'session-id-time': '2082787201l'}
        URL = self.url_template(search_item, page)
        HEADERS = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
    }
        response = requests.get(URL, headers=HEADERS, cookies=cookies)
        return response.content, response


    def amazon_find_text(self, first_class_name, soup):
        
        data = []
        divs = soup.find_all("div", {"class":first_class_name})
        for div in divs: 
            _temp = {} 
            name_div = div.find("div", {"class":"a-section a-spacing-none s-padding-right-small s-title-instructions-style"})
            if name_div:
                _temp['name'] = name_div.h2.a.text
                _temp['link'] = name_div.h2.a['href']
            price_div = div.find("div", {"class":"a-row a-size-base a-color-base"})
            if price_div:
                _temp['price']=price_div.find('span', {"class":"a-price-whole"}).text
            else:
                _temp['price']=None 
            star = div.find("span", {"class":"a-icon-alt"})
            if star:
                _temp["star"] = star.text
            else:
                _temp["star"] = None
            rating = div.find("span", {"class":"a-size-base s-underline-text"})
            if rating:
                _temp["rating"] = rating.text
            else:
                _temp["rating"] = None
            if _temp and _temp["price"]: 
                data.append(_temp) 
        return data
    
    def get_amazon_bulk_data(self, n, search_item):
        #driver = webdriver.Chrome(self.path)
        data = {}
        print("start scraping.....")
        for page in range(1, n):
            
            print()
            print("wait..") 
            

            page_content, response_d = self.get_html_content(search_item, page)
            #URL = self.url_template(search_item, page)
            print(response_d)
            #driver.get(URL)
            soup = BeautifulSoup(page_content, "html.parser")

            if response_d.status_code == 200:
                print(f"succefully page {page} has been scrapped ")
            else:
                print(f"there is {response_d.status_code} error in this page!! ")
            
            div = self.amazon_find_text("a-section a-spacing-small a-spacing-top-small", soup)
            data[page] = div
            time.sleep(0)
            print("done..")
        print("scraping over")
        return data 