import requests
from bs4 import BeautifulSoup

url='https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&from_source=nav_search_new'


response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
targets=soup.find_all("li",class_='so-icon time')
a=1
for target in targets:
    print(a)
    a+=1
    print(target.text)