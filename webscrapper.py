"""
    NOTE:- This code only works if the Pixelford's blog website is not edited 
    if the website is edited and the tags or classes which is used in this code is changed directly from the website
    then the code is pretty much useless
"""
import requests
from bs4 import BeautifulSoup
import datetime
url="https://pixelford.com/blog/"
response=requests.get(url,headers={'user-agent':'Hello'}) #changing user agent because the website got too many requests from python header leading it to block every requests which had the name python as its header
html=response.content   #gets the html of the website
soup=BeautifulSoup(html,'html.parser')  #organizes the code
contents=soup.find_all('article',class_="type-post") #gets everything from the article tag 
for content in contents:
    blog_title=content.find('a',class_="entry-title-link").getText()    #getting the titles only
    blog_dateTime=content.find('time',class_="entry-time").get('datetime') #getting the date time format as a string
    convertDatetime=datetime.datetime.fromisoformat(blog_dateTime) #converting date and time from string to a real date and time
    customDateTime=convertDatetime.strftime("%b-%d,%Y") #custom string format for creating our own date and time format
    print(f"{customDateTime} - {blog_title}")   #final display