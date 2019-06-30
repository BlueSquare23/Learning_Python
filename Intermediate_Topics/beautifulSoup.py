#!/usr/bin/python3
#Playing with beautifulSoup

import requests
from bs4 import BeautifulSoup

#Uses requests to get the html of a page
url = 'https://newyorktimes.com'
r = requests.get(url)
r_html = r.text

#Saves that html string as a BeautifulSoup object
#(Also specifies the parser to be used)
soup = BeautifulSoup(r_html, "html.parser")

#Prints out all of the links on the page
for link in soup.find_all('a'):
    print(link.get('href'))
