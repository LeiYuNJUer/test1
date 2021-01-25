#beautifulsoup4 将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳成4种：
#
# 1. tag 标签及其内容：拿到第一个内容
# 2. navigablestring
# 3. beautifulsoup
# 4. comment

from bs4 import BeautifulSoup
import re

file = open("./weibo1.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")


#tag
print(bs.title)
print(bs.a)
print(bs.head)
print(type(bs.head))

# 2. navigablestring  标签里的内容 字符串
print(bs.title.string)
print(type(bs.title.string))

print(bs.a.attrs)

# 3. beautifulsoup 表示整个文档
print(bs.attrs)
print(bs.name)
print(bs)


# 4. comment是个特殊的navigablestring 不包含注释符号
print(bs.a.string)

#---------------------------------------
#应用
#文档的遍历

#文件的搜索

#查找所有
#字符串过滤，查找所有与字符串匹配的内容
t_list = bs.find_all("a")
print(t_list)

#正则表达式搜索
t_list = bs.find_all(re.compile("a"))

#kwargs
t_list = bs.find_all(id="head")
for item in t_list:
    print(item)

#text参数
t_list = bs.find_all(text = ["hao123"])
t_list = bs.find_all(text = re.compile("\d"))


#limit参数

t_list = bs.find_all("a",limit= 3)


#css选择器
#标签 类名 id 属性等等
t_list = bs.select('title')



