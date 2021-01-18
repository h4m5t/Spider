#爬取指定网页的一张图片
#placekitten.com
import urllib.request

response=urllib.request.urlopen('http://placekitten.com/300/400')

catimg=response.read()

with open('pictures\\cat1.jpg','wb') as f:
    f.write(catimg)
