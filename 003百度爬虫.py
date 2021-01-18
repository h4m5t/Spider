from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve
html=urlopen("http://www.baidu.com/")

#用beautifulsoup解析HTML
obj=bf(html.read(),'html.parser')

title=obj.head.title

#print(title)
logo=pic_info=obj.find_all('img',class_="index-logo-src")

logo_url = "https:"+logo[0]['src']
print(logo_url)

urlretrieve(logo_url, '爬虫/logo.png')