import requests
from app.urls.amazon_urls import urls
from bs4 import BeautifulSoup as BS
from app.models import Model


class AmazonController:
    def __init__(self):
        self.model_laptop = Model(coll_name='laptops', db_name='Amazon')
        self.model_mobile = Model(coll_name='mobiles', db_name='Amazon')

    def laptop_search(self):
        search_url = urls['laptops']
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        soup = BS(response.content, 'html5lib')
        ans = soup.find_all("div", attrs={"class": "_1AtVbE"})

        # returning the price
        return ans.prettify()

    def mobile_search(self):
        search_url = urls['mobiles']
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        soup = BS(response.content, 'html5lib')
        ans = soup.find("div", attrs={"class": "s-search-results"}).text

        # returning the price
        return ans
