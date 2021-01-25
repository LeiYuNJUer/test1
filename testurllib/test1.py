import urllib.request
import urllib.parse

#获取一个get请求
#response = urllib.request.urlopen("https://www.baidu.com/")
#print(response.read().decode('utf-8')) #对获取到的网站源码进行一个utf—8解码

#获取一个post请求
# data = bytes(urllib.parse.urlencode({"fuck":"you"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))

# #超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout= 0.001)
#     print(response.read().decode("utf-8"))
# except :
#     print("time out!")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheaders())

#伪装自己
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
#url = "http://www.douban.com"
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"fuck":"you"}), encoding="utf-8")
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# }
# req = urllib.request.Request(url = url, data = data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://weibo.com/newsxh?is_all=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.141 Safari/537.36 "
}
req = urllib.request.Request(url = url,headers= headers)
response = urllib.request.urlopen(req)
print(response.read().decode("GBK"))


