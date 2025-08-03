import requests
url="https://pixelford.com/blog/"
response=requests.get(url,headers={'user-agent':'Hello'})
print(response.content)
