import re
import requests
from bs4 import BeautifulSoup


url="http://top.baidu.com/buzz?b=353&fr=topindex"
html=requests.get(url)

html.encoding = 'gb18030' 
sp=BeautifulSoup(html.text,'html.parser')




f=open("result.txt","w",encoding="utf-8")
lists=sp.find_all("a","list-title")
count=1
for i in lists:
    s=str(count)+" "+i.string+"\n"
    print(s)
    f.write(s)
    count+=1
    
    
