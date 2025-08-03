import requests
from bs4 import BeautifulSoup
url="https://pixelford.com/blog/"
response=requests.get(url,headers={'user-agent':'Hello'}) #changing user agent because the website got too many requests from python header leading it to block every requests which had the name python as its header
html=response.content
soup=BeautifulSoup(html,'html.parser')
a_tags=soup.find_all('a',class_="entry-title-link")
for a in a_tags:
    print(a)