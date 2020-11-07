import urllib.request
import urllib.parse
import json
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'


head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
print("欢迎来带翻译程序！！！")
while True:
    data={}
    data['doctype']='json'

    content=input("请输入你要翻译的内容(---输入-1退出程序---)：")

    if content=='-1':
        break
    else:

        data['i']=content

        data=urllib.parse.urlencode(data).encode('utf-8')
        
        req=urllib.request.Request(url,data,head)

        response=urllib.request.urlopen(req)

        html=response.read().decode('utf-8')

        target=json.loads(html)

        #print(req.headers)
        
        print('\n')
        print(target['translateResult'][0][0]['tgt'])
        print('\n')












