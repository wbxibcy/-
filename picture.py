import os
import time

import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
AllUrl = 'https://www.vmgirls.net/'

BS = BeautifulSoup(requests.get(AllUrl, headers=headers).text, 'lxml')

allurl = BS.find_all('a', {'href':re.compile('https\:\/\/www\.vmgirls\.net\/.*\.html')})
for i in allurl:
    # print(i['href'])

    response = requests.get(i['href'], headers=headers)
    html = response.text

    bs = BeautifulSoup(html, 'lxml')
    # print(bs)

    dir_name = bs.find('h1', {'class':'post-title mb-3'}).get_text()
    # print(dir_name)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    urls = bs.find_all('img')
    # for url in urls:
    #     print(url['src'])

    for url in urls:
        try:
            time.sleep(1)  
            file_name = url['src'].split('/')[-1]
            if url['src'].split('.')[-1] != 'jpeg' and url['src'].split('.')[-1] != 'jpg' and url['src'].split('.')[-1] != 'png':
                continue
            else:
                response = requests.get(url['src'], headers=headers)
            with open(dir_name + '/' + file_name, 'wb') as f:  
                f.write(response.content)
        except OSError:
            pass

print('好耶!!!')