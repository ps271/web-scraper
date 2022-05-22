from bs4 import BeautifulSoup as BS
import requests
from app.urls.amazon_urls import urls


def laptops():
    search_url = urls['laptops']
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BS(response.content, 'html5lib')
    #ans = soup.find("div", attrs={"class": "s-search-results"}).text
      
    # returning the price
    return soup.prettify()
  
# method to get the price of bit coin
def get_price(url):
      
    # getting the request from url

    data = requests.get(url)
  
    # converting the text 
    soup = BS(data.text, 'html5lib')
  
    # finding metha info for the current price
    ans = soup.find("div", class_ ="BNeawe iBp4i AP7Wnd").text
    state = soup.find("span", class_ ="iXabQc ASafz")
    print(state)
      
    # returning the price
    return ans

if __name__ == "__main__":
    url = "https://www.google.com/search?q=bitcoin+price"
    r = laptops()
    print(r)