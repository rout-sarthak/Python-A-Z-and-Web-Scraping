# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:23:16 2019

@author: sarthak
"""

import requests
from bs4 import BeautifulSoup

result = requests.get("https://screenrant.com/")
src = result.content
soup = BeautifulSoup(src)

#making an empty list for getting all the URLs (news articles)
urls = []
for h3_tag in soup.find_all("h3"): 
    a_tag = h3_tag.find('a')
    try:
        if 'href' in a_tag.attrs:
            urls.append(a_tag.attrs['href'])
    except:
        pass
    
print(urls)