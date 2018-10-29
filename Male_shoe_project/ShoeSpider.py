import re
import os
import sqlite3
import json
from bs4 import BeautifulSoup
import urllib
import urllib.request
import ssl

def creatDatabase():
    dbPath = 'shoe.sqlite'
    if os.path.exists(dbPath):
       os.remove(dbPath)
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    # 创建表
    cursor.execute('''create table t_sales
                (id integer primary key autoincrement not null,
                color text not null,
                size text not null,
                source text not null,
                discuss mediumtext not null,
                time text not null);''')
    conn.commit()
    conn.close()



#获取评论区的json数据
def getRateDetail(itemId,currentPage):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId='+ str(itemId) + '&spuId=916810354&sellerId=890482188&order=3&currentPage=' + str(currentPage) + '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvfpvWvRhvUvCkvvvvvjiPR2sOAjrmRFcpsjEUPmPyQjnhPFswtjECPFzZgjtn9phv2nM5o2QX7rMNzsFfz86Cvvyv9njxevvvCXejvpvhvUCvp2yCvvpvvhCvvphvC9vhphvvvUyCvvOCvhECzWmivpvUvvCCEY8I%2B5mtvpvIvvCvxQvvvb6vvhoCvvmv1pvvBJZvvUHmvvCHtpvv9BpvvhoCvvmCy9yCvhAv2i7xjaVTRLwp8BLhACy7RqwiLO2v5fVQKoZH1nvaRfUTnZJt9b8rV8tYVVzvdiZB%2BmWC%2B87JeCywahJQ0fJ6W3CQog0HKfUpejxP2QhvCvvvMM%2F5vpvhvvCCB2yCvvpvvhCv&needFold=0&_ksTS=1540620973179_636&callback=jsonp637'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    # 设置忽略证书的选项
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    html = response.read().decode("utf-8")
    # print(type(html))
    c = html.replace('jsonp637(', '')
    c = c.replace(')', '')
    c = c.replace('false', '"false"')
    c = c.replace('true', '"true"')
    tmalljson = json.loads(c)
    return tmalljson

#获取ItemID号
def getProductIdList(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    # 设置忽略证书的选项
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    html = response.read().decode("GB18030")
    soup = BeautifulSoup(html,'html.parser')
    linkList = []
    idList = []
    tags = soup.find_all(href=re.compile('detail.tmall.com/item.htm'))
    for tag in tags:
        linkList.append(tag['href'])
    linkList = list(set(linkList))
    for link in linkList:
        aList = link.split('&')
        idList.append(aList[0].replace('//detail.tmall.com/item.htm?id=',''))
    return idList

#获取评论区总页数
def getLastPage(itemId):
    tmalljson = getRateDetail(itemId,1)
    return tmalljson['rateDetail']['paginator']['lastPage']

def writeInSqlite3(productIdList):
    dbPath = 'shoe.sqlite'
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    initial = 0
    while initial < len(productIdList):
        try:
            itemId = productIdList[initial]
            print('----------',itemId,'------------')
            maxnum = getLastPage(itemId)
            num = 1
            while num <= maxnum:
                try:
                    tmalljson = getRateDetail(itemId, num)
                    rateList = tmalljson['rateDetail']['rateList']
                    n = 0
                    while n < len(rateList):
                        colorSize = rateList[n]['auctionSku']
                        m = re.split('[:;]',colorSize)
                        rateContent = rateList[n]['rateContent']
                        color = m[1]
                        size = m[3]
                        dtime = rateList[n]['rateDate']
                        cursor.execute('''insert into t_sales(color,size,source,discuss,time)
                                        values('%s','%s','%s','%s','%s') ''' % (color,size,'天猫',rateContent,dtime))
                        conn.commit()
                        n += 1
                    num += 1
                except Exception as e:
                    continue
            initial += 1
            print('--------over---------')
        except Exception as e:
            print(e)

    conn.close()


def main():
    creatDatabase()
    url_name = ['40657ec4RpVoqI','0.6f6a7ec4hCBowr&s=60','0.65d77ec4OcLq0z&s=120','0.643f7ec4eKaPmS&s=180','0.7d727ec4OPjVtE&s=240']
    for i in url_name:
        url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.'+str(i)+'&q=%C4%D0%D0%AC&sort=d&style=g&from=..pc_1_searchbutton&active=2&type=pc'
        productIdList = getProductIdList(url)
        writeInSqlite3(productIdList)

if __name__ == '__main__':
    main()