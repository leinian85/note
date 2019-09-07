[TOC]



## spider

#### 1.请求模块 urllib.request

```python
url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
# url请求头包装
urllib.request.Request(url = url,headers = headers)
# url请求
res = urllib.request.urlopen(url)
res.read() # 获取响应的内容
res.geturl() # 获取响应的链接
res.code() # 获取响应的响应码
```

#### 2.编码模块(中文编码) urllib.parse

```python
# 1.字典编码
params = {"wd":"赵丽颖","pn":"10"}
paramsb = parse.urlencode(params)
print(paramsb) # wd=%E8%B5%B5%E4%B8%BD%E9%A2%96&pn=10
# 2.字符串编码
word = "赵丽颖"
wordb = parse.quote(word)
print(wordb) # %E8%B5%B5%E4%B8%BD%E9%A2%96
```



```python
# 场景:获取中文的 url
from urllib import parse
baseurl = "https://www.baidu.com/s?"
# 字典编码
params = {"wd":"赵丽颖","pn":"10"}
result = parse.urlencode(params)
url = baseurl + result
print(url) # https://www.baidu.com/s?wd=%E8%B5%B5%E4%B8%BD%E9%A2%96&pn=10
```

#### 3.fake_useragent 模块

```python
# 提供 User-Agent ,需要下载
# eg.
from fake_useragent import UserAgent
us = UserAgent()
print(us.random)
```

#### 4.re 模块

- 贪婪模式和非贪婪模式





**初级爬虫工程师**：

```shell
1. Web前端的知识：HTML, CSS, JavaScript, DOM, DHTML, Ajax, jQuery,json等；
2. 正则表达式，能提取正常一般网页中想要的信息，比如某些特殊的文字，链接信息，知道什么是懒惰，什么是贪婪型的正则；
3. 会使用re, BeautifulSoup，XPath等获取一些DOM结构中的节点信息；
4. 知道什么是深度优先，广度优先的抓取算法，及实践中的使用规则；
5. 能分析简单网站的结构，会使用urllib或requests库进行简单的数据抓取；
```

  **中级爬虫工程师**：

```shell
1. 了解什么是Hash，会使用简单的MD5,SHA1等算法对数据进行Hash以便存储；
2. 熟悉HTTP,HTTPS协议的基础知识,了解GET，POST方法,了解HTTP头中的信息，包括返回状态码，编码，user-agent，cookie，session等；
3. 能设置User-Agent进行数据爬取，设置代理等；
4. 知道什么是Request，什么是Response，会使用Fiddler, Wireshark等工具抓取及分析简单的网络数据包；对于动态爬虫，要学会分析Ajax请求，模拟制造Post数据包请求，抓取客户端session等信息，对于一些简单的网站，能够通过模拟数据包进行自动登录；
5. 对于比较难搞定的网站，学会使用浏览器+selenium抓取一些动态网页信息；
6. 并发下载，通过并行下载加速数据抓取；多线程的使用；
```

  **高级爬虫工程师**：

```shell
1. 能使用Tesseract，百度AI, HOG+SVM,CNN等库进行验证码识别；
2. 能使用数据挖掘的技术，分类算法等避免死链等；
3. 会使用常用的数据库进行数据存储，查询，如Mongodb，Redis(大数据量的缓存)等；下载缓存，学习如何通过缓存避免重复下载的问题；Bloom Filter的使用；
4. 能使用机器学习的技术动态调整爬虫的爬取策略，从而避免被禁IP封号等；
5. 能使用一些开源框架Scrapy, Scarpy-Redis，Celery等分布式爬虫，能部署掌控分布式爬虫进行大规模的数据抓取
```