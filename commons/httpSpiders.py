# -*- coding: utf-8 -*-
# 爬取页面信息
import requests ,re, sqlite3
ENDREC = 'endrec.'
url = 'https://www.bilibili.com/'
headerObj = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
response = requests.get(url=url,headers = headerObj)
htmlText = response.text
files = open('list.txt','w',encoding='utf-8')
# html_data = re.findall('"title":"(.*?)"',htmlText)
html_data = re.findall('{"id":(.*?),"bvid":"(.*?)","cid":(.*?),"goto":"(.*?)","uri":"(.*?)","pic":"(.*?)","title":"(.*?)\n?(.*?)","duration":[0-9]*,"pubdate":[0-9]*,"owner":{"mid":[0-9]*,"name":"(.*?)","face":"http:(.*?)"},"stat":{"view":[0-9]*,"like":[0-9]*},"av_feature":(.*?)}',htmlText)
for listPojo in html_data:
    if listPojo != "":
        # 打印并写入指定的file
        print(listPojo,file=files)

