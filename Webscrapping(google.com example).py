# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 16:07:41 2019

@author: sarthak
"""

import requests
from bs4 import BeautifulSoup #importing BeautifulSoup class

result = requests.get("https://www.google.com/")
#To ensure that the website is accessible we use status_code to obtain a result 
#of 200 OK

print(result.status_code) #it gives 200 as output which means that the website is accessible

print(result.headers) #getting some more random data to ensure that the content on website is accessible without any issues

#result.content will give the source of the website and we can store it in a variable
src = result.content
print(src) #this step is not necessary , but, just in case 

#Now we have to create an object using BeautifulSoup and passing the source (src) through it
soup = BeautifulSoup(src)

#if we want to find all the links on the page, then
links = soup.find_all("a") #Here a is the a tag which precedes links on html pages
print(links)

#Now, if we want to extract the a-tag that contains the text "About" then,
for link in links:
    if "Maps" in link.text:
        print(link)
        print(link.attrs['href'])
