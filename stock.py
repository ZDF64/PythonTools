# -*- coding: utf-8 -*-
# 爬取页面信息
import requests ,re, sqlite3
ENDREC = 'endrec.'
url = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,200&dt=1638433912533&atfc=&onlySale=0'
headerObj = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
response = requests.get(url=url,headers = headerObj)
htmlText = response.text
files = open('stockList.txt','w',encoding='utf-8')
# html_data = re.findall('"title":"(.*?)"',htmlText)
html_data = re.findall('\["[0-9]{6}","[/u4e00-\u9fa5\(\)()\da-zA-Z0-9&]{2,50}","[A-Z0-9]*","[0-9]{0,2}","[0-9]{0,2}","[0-9\.]{0,9}","[0-9\.]{0,9}","[0-9]{0,3}","[0-9]{0,3}","\w{0,4}","\w{0,4}","[0-9]{0,3}","[0-9]{0,3}","[0-9]{0,3}","[0-9]{0,3}","[0-9]{0,3}","[0-9]{0,3}","[0-9\.\%]{0,9}","[0-9\.\%]{0,9}","[0-9]{0,3}","[0-9\.\%]{0,9}"\]',htmlText)
for listPojo in html_data:
    if listPojo != "":
        # 打印并写入指定的file
        print(listPojo,file=files)
        # print(listPojo)