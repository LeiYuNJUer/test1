#-*- coding = utf-8 -*-

from bs4 import BeautifulSoup
import re
import xlwt
import urllib
import sqlite3
import json
import requests


def main():
    #baseurl = "https://weibo.com/newsxh?is_all=1"
    baseurl = "https://m.weibo.cn/comments/hotflow?id=4596570748625630&mid=4596570748625630&max_id_type=0"
    #1.爬取网页
    #dataList = getData(baseurl)
    #2.（逐一）解析数据
    #savepath = ".\\新华网微博.xls"
    #3.保存数据
    #saveData(savepath)
    #askUrl(baseurl)
    cookies = {"cookie":" WEIBOCN_FROM=1110006030; SUB=_2A25ND8lDDeRhGeNH4lAQ8SrEwziIHXVu89cLrDV6PUJbkdAfLU3YkW1NSndRx2ljM8vApUS_X6vTnKWnw6NNPXbs; _T_WM=40826094050; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4596570748625630%26luicode%3D20000061%26lfid%3D4596570748625630%26uicode%3D20000061%26fid%3D4596570748625630; XSRF-TOKEN=b085a4"}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    url = baseurl
    response = requests.get(url,headers=headers,cookies=cookies)
    jsondata = response.json()
    data = jsondata.get("data")
    #print(data)
    print(response.text)
#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,25):
        url = baseurl + str(i*25)
        html = askUrl(baseurl)

    #2.逐一解析数据
    return datalist

#得到指定一个url的网页内容
def askUrl(url):
    head = {#模拟浏览器头部信息
        "user - agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.141Safari / 537.36"
    }
    #用户代理， 告诉微博 我们是什么机器 浏览器（告诉浏览器，我们可以接受什么类型的文件内容）

    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


def saveData(savepath):
    print("save....")

if __name__ == "__main__":
    main()