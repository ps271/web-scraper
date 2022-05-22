from flask import Blueprint, jsonify
import requests
from app.urls.amazon_urls import urls
from bs4 import BeautifulSoup as BS


amazon_bp = Blueprint('api/amazon', __name__, url_prefix='/webscraper/amazon')


@amazon_bp.route('/laptops', methods=['GET'])
def laptops():
    search_url = urls['laptops']
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BS(response.content, 'html5lib')
    ans = soup.find("div", attrs={"class": "s-search-results"}).text

    # returning the price
    return ans


@amazon_bp.route('/mobiles', methods=['GET'])
def mobiles():
    search_url = urls['mobiles']
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BS(response.content, 'html5lib')
    ans = soup.find("div", attrs={"class": "s-search-results"}).text

    # returning the price
    return ans
