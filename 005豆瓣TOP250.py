import requests
from bs4 import BeautifulSoup

def writefile(targets,f):
    for target in targets:
        print(target.a.span.text)
        f.writelines(target.a.span.text+'\n')

def get_response(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    targets=soup.find_all("div",class_='hd')
    return targets

f=open('douban.txt','w',encoding='utf-8')
url='https://movie.douban.com/top250?start=0&filter='

for i in range(10):
    print(f"---------正在爬取第{i+1}页----------")
    url='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    #print(url)
    targets=get_response(url)
    writefile(targets,f)

f.close()






