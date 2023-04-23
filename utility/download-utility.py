# Utility file to downlad files from nse
from urllib.parse import urlparse

headers = {
           'accept-encoding': 'gzip, deflate, sdch, br',
           'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
           }
# 'X-Requested-With': 'XMLHttpRequest'

cookies_dict = {"bm_sv": "25D0AE3704837670AB1474E685D69494~2+VQgEwxJ1O8BAf8wp/9KUOh7YCWEESJhbtQ/FFtldFOcHxGpZvtD2T7o3HQQRd4wXaHRCaZ6f6E49zRaHOQLGU7huWuOCxlYkIGFV6Mp/ZtF4INM8yCg7nGPVY3SZ2UykX7EnkydYnjpRU3SKwKoPQ5PpfxIfsEDwY/zWryb1o="}
import requests

def download_file(url,*args,**kwargs):
    url = 'https://www.nseindia.com/api/historical/cm/equity?symbol=TATAMOTORS&series=["EQ"]&from=21-01-2021&to=21-07-2021&csv=true'
    url1 = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=RELIANCE'
    session = requests.Session()
    session.headers.update(headers)
    # session.cookies.update(cookies_dict)
    # parsed_url = urlparse(url)
    # session.headers.update({'Host': parsed_url.hostname})
    # if self.method == 'get':
    response = session.get(url1 )
    # response = requests.get(url,headers=headers)
    content = response.content
    csv_file = open("TATAMOTORS.csv", "wb")
    csv_file.write(content)
    csv_file.close()
    print(csv_file)

    # URLFetchSession(url)
    pass

download_file('a')