import re
from bs4 import BeautifulSoup
import requests

origin_url="http://bang.dangdang.com/books/bestsellers/01.54.00.00.00.00-year-2020-0-1-"

f=open("result_books.txt","w",encoding="utf-8")

for i in range(1,26):
    
    url=origin_url+str(i)

    html=requests.get(url)
    #html.encoding="gb18030"
    sp=BeautifulSoup(html.text,"html.parser")
    name_lists=sp.find_all("div","name")
    author_lists=sp.find_all("div","publisher_info")
    price_lists=sp.find_all("span","price_n")
    # for i in name_lists:
    #     print(i.a.string)

    # for i in price_lists:
    #     print(i.string)

    # for i in author_lists:
    #     print(i.a.string)

    
    for j in range(20):
        print((i-1)*20+j+1)
        print("----------------------------------------")
        print(name_lists[j].a.string,end=" ")
        print(author_lists[2*j].a.string,end=" ")
        print(author_lists[2*j+1].a.string,end=" ")
        print(price_lists[j].string,end=" ")
        print("\n")




