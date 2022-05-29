import json
import requests
from app.urls.flipkart_urls import urls
from bs4 import BeautifulSoup as BS
from app.models import Model
import time


class FlipkartController:
    def __init__(self):
        self.model_laptop = Model(coll_name='laptops', db_name='Flipkart')
        self.model_mobile = Model(coll_name='mobiles', db_name='Flipkart')
        self.base_url = 'https://www.flipkart.com'

    def get_search_result(self, search_url):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        return response

    def laptop_search(self):
        self.model_laptop.delete_all()
        search_url = urls['laptops']
        response = self.get_search_result(search_url=search_url)
        soup = BS(response.content, 'html5lib')
        laptops = soup.find_all("div", attrs={"class": "_1AtVbE"})
        laptops = list(laptops)
        laptops = laptops[3:]
        for laptop in laptops:
            laptop_page_link = laptop.select_one('._1fQZEK')['href']
            laptop_page_link = f'{self.base_url}{laptop_page_link}'
            laptop_page = self.get_search_result(laptop_page_link)
            soup = BS(laptop_page.content, 'html5lib')
            title = soup.find("span", attrs={"class": "B_NuCI"}).text
            images = soup.find_all("img", attrs={"class": "q6DClP"})
            image_links = []
            for image in images:
                img_link = image['src']
                image_links.append(img_link)
            amount = soup.find("div", attrs={"class": "_3I9_wc"}).text
            price = soup.find("div", attrs={"class": "_30jeq3"}).text
            am = amount[1:]
            am = am.split(',')
            am = ''.join(am)
            pr = price[1:]
            pr = pr.split(',')
            pr = ''.join(pr)
            discount = str(((int(am) - int(pr))*100//int(am))) + '%'
            rating = soup.find("div", attrs={"class": "_3LWZlK"}).text
            specifications = soup.find_all("div", attrs={"class": "_3k-BhJ"})
            specs = {}
            for specification in specifications:
                table_name = specification.select_one('.flxcaE').text
                table = specification.find_next("tbody")
                table = list(table)
                k_v = {}
                for row in table:
                    key = row.select_one('._1hKmbr').text
                    value = row.select_one('._21lJbe').text
                    k_v[key] = value
                specs[table_name] = k_v
            post_data = {}
            post_data['title'] = title
            post_data['images'] = image_links
            post_data['amount'] = amount
            post_data['price'] = price
            post_data['discount'] = discount
            post_data['rating'] = rating
            post_data['specifications'] = specs
            self.model_laptop.add(post_data)
            time.sleep(2)
        # returning the price
        return {'success': 'OK'}

    def mobile_search(self):
        # self.model_mobile.delete_all()
        search_url = urls['mobiles']
        response = self.get_search_result(search_url=search_url)
        soup = BS(response.content, 'html5lib')
        mobiles = soup.find_all("div", attrs={"class": "_1AtVbE"})
        mobiles = list(mobiles)
        mobiles = mobiles[3:]
        for mobile in mobiles:
            mobile_page_link = mobile.select_one('._1fQZEK')['href']
            mobile_page_link = f'{self.base_url}{mobile_page_link}'
            mobile_page = self.get_search_result(mobile_page_link)
            soup = BS(mobile_page.content, 'html5lib')
            title = soup.find("span", attrs={"class": "B_NuCI"}).text
            images = soup.find_all("img", attrs={"class": "q6DClP"})
            image_links = []
            for image in images:
                img_link = image['src']
                image_links.append(img_link)
            amount = soup.find("div", attrs={"class": "_3I9_wc"}).text
            price = soup.find("div", attrs={"class": "_30jeq3"}).text
            am = amount[1:]
            am = am.split(',')
            am = ''.join(am)
            pr = price[1:]
            pr = pr.split(',')
            pr = ''.join(pr)
            discount = str(((int(am) - int(pr)) * 100 // int(am))) + '%'
            rating = soup.find("div", attrs={"class": "_3LWZlK"}).text
            specifications = soup.find_all("div", attrs={"class": "_3k-BhJ"})
            specs = {}
            for specification in specifications:
                table_name = specification.select_one('.flxcaE').text
                table = specification.find_next("tbody")
                table = list(table)
                k_v = {}
                for row in table:
                    key = row.select_one('._1hKmbr').text
                    value = row.select_one('._21lJbe').text
                    k_v[key] = value
                specs[table_name] = k_v
            post_data = {}
            post_data['title'] = title
            post_data['images'] = image_links
            post_data['amount'] = amount
            post_data['price'] = price
            post_data['discount'] = discount
            post_data['rating'] = rating
            post_data['specifications'] = specs
            self.model_mobile.add(post_data)
            time.sleep(2)
        # returning the price
        return {'success': 'OK'}
