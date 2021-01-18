import requests
from bs4 import BeautifulSoup

def get_url(n):
    '''获取url，n<30'''
    return 'https://www.thepaper.cn/load_index.jsp?nodeids=26490&topCids=&pageidx='+str(n)+'&isList=true&lastTime=1606096323374'

def get_urllist():
    url_list = []
    for i in range(30):
        url=get_url(i)
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        urllist=soup.find_all(class_='news_li')

        #print(len(urllist))
        for i in urllist:
            if i.h2:
                news_id=i.h2.a.get('href')
                #print(news_id)
                url_list.append(news_id)
    return url_list


async def gen_url():
    url_list=get_urllist()
    for each_id in range(200):
        yield "https://www.thepaper.cn/{}".format(url_list[each_id])

async def parse(response):
    return response.xpath('//meta[@name="title"]/@content')[0]
       

if __name__ == "__main__":
    #url_list=get_urllist()
    pass