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

def save_file(filename,content):
    filepath=f'news/汽车圈/{filename}.txt'
    try:
        f=open(filepath,'w',encoding='utf-8')
        #f.write(title.text)
        f.write(content)
        f.close()
    except OSError as e:
        print(e.args)

if __name__ == "__main__":
    url_list=get_urllist()
    print(url_list)
    for i in range(200):
        news_url='https://www.thepaper.cn/'+url_list[i]
        #print(news_url)
        response=requests.get(news_url)
        soup=BeautifulSoup(response.text,"html.parser")

        title=soup.find(class_='news_title')
        #print(title.text)
        txt=soup.find(class_='news_txt')
        #print(txt.text)
        try:
            save_file(title.text,txt.text)
        except AttributeError as e:
            print(e.args)
