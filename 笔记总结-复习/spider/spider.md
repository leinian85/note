[TOC]



## spider

### 1.请求模块 urllib.request

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

### 2.编码模块(中文编码) urllib.parse

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

### 3.fake_useragent 模块

```python
# 提供 User-Agent ,需要下载
# eg.
from fake_useragent import UserAgent
us = UserAgent()
print(us.random)
```

### 4.re 模块

- 贪婪模式和非贪婪模式

### 5.csv模块

```python
writerow([])           # 列表中每个元素代表csv中每一列
writerows([(),(),()])  # 元组中每个元素代表csv中每一列,也可以是列表
writerows([[],[],[]])  # 元组中每个元素代表csv中每一列,也可以是列表
```

```python
# 将文件保存到csv文件
import csv
file = [
    ("霸王别姬","张国荣,张丰毅,巩俐","1993-01-01"),
    ("肖申克的救赎","蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿","1994-09-10"),
    ("罗马假日","格利高里·派克,奥黛丽·赫本,埃迪·艾伯特","1953-09-02")
]
# 方法一:一行一行写入
# newline="" 避免在 windows 系统中出现空行
def sava_csv(self,file):
    with open("猫眼电影.csv","w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["名称", "主演", "上映时间"])
        for line in file:
            writer.writerow(line)
# 方法二:一次性写入
def save_csv_rows(self,file):
    with open("猫眼电影.csv","w",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(file)

```

### 6.pymysql模块

```python
# 将数据保存到 mysql,使用 executemany 比使用 execute 效率要高
import pymysql
file = [
    ("霸王别姬","张国荣,张丰毅,巩俐","1993-01-01"),
    ("肖申克的救赎","蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿","1994-09-10"),
    ("罗马假日","格利高里·派克,奥黛丽·赫本,埃迪·艾伯特","1953-09-02")
]
def save_mysql(self,file):
    db = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="spider",
            port=3306,
            charset='utf8'
        )
    cursor = db.cursor()
    sql = "insert into filmtab(name,star,time) values(%s,%s,%s)"
    cursor.executemany(sql,file)  # 一次性将数据保存,file可以为列表,元组
    db.commit()
    cursor.close()
    db.close()
save_mysql(file)
```

### 7.xpath模块

### 8.requests模块

### 9.selenium模块

```python
selenium + PhantomJS / Chrome / Firefox 可以模拟浏览器操作
```

```python
# 代码示例1:
from selenium import webdriver
import time

browser = webdriver.PhantomJS()  # 打开phantomjs浏览器
browser.get("http://www.baidu.com") # 访问百度
browser.save_screenshot('baidu.png') # 照快照
time.sleep(5)
browser.quit() # 关闭浏览器
```

####     1. 常用操作

```python
# 1、键盘操作
from selenium.webdriver.common.keys import Keys
node.send_keys(Keys.SPACE)
node.send_keys(Keys.CONTROL, 'a')
node.send_keys(Keys.CONTROL, 'c')
node.send_keys(Keys.CONTROL, 'v')
node.send_keys(Keys.ENTER)

# 2、鼠标操作
from selenium.webdriver import ActionChains
mouse_action = ActionChains(browser)
mouse_action.move_to_element(node)
mouse_action.perform()

# 3、切换句柄
all_handles = browser.window_handles
browser.switch_to.window(all_handles[1])

# 4、iframe子框架
browser.switch_to.iframe(iframe_element)

# 5、Web客户端验证
url = 'http://用户名:密码@正常地址'
```



####     2. 无界面模式(代码示例)

```python
# 代码示例2: 京东爬图书
from selenium import webdriver
import time

class JdSpider:
    def __init__(self):
        self.url = "https://www.jd.com/"
        options = webdriver.ChromeOptions() # 无界面模式
        options.add_argument('--headless')  # 无界面模式
        self.browsder = webdriver.Chrome(options = options)
        self.books = []

    def get_html(self,key):
        self.browsder.get(self.url)
        sel = self.browsder.find_element_by_xpath('//*[@id="key"]')
        sel.send_keys(key)
        fnd = self.browsder.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        fnd.click()
        time.sleep(3)

    def parse_html(self):
        self.browsder.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        ) # 执行script代码,鼠标滑到最下面,让页面全部加载出来
        time.sleep(3)

        li_list = self.browsder.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')

        for li in li_list:

            abook = {}
            price = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            title = li.find_element_by_xpath('.//div[@class="p-name"]').text.strip()
            market = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            abook["price"] = price
            abook["title"] = title
            abook["market"] = market
            print(abook)
            self.books.append(abook)
        print(len(self.books))

    def run(self,ksy):
        self.get_html(ksy)
        self.parse_html()
        for i in range(3):
            if self.browsder.page_source.find("pn-next disable") == -1:
                self.browsder.find_element_by_class_name('pn-next').click()
                time.sleep(3)
                self.parse_html()
            else:
                break

js = JdSpider()
js.run('爬虫')
```

####     3. 模拟鼠标移动(代码示例)

```python
# 代码示例3:模拟鼠标移动
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
set_node = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')

mouse_obj = ActionChains(browser)
mouse_obj.move_to_element(set_node)
mouse_obj.perform()

browser.find_element_by_link_text('高级搜索').click()
```

####     4. 句柄切换(代码示例)

```python
# 代码示例4:句柄切换,爬行政区域编号
from selenium import webdriver
import pymysql

class GovSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            database='blog',
            port=3306,
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        self.browser = webdriver.Chrome()
        self.province = []  # 省
        self.city = [] # 市
        self.county = [] # 区

    def get_data(self):
        self.browser.get(self.url)
        xpath_dbs = '//td[@class="arlisttd"]/a[contains(@title,"行政区划代码")]'
        a = self.browser.find_element_by_xpath(xpath_dbs)
        href = a.get_attribute("href")

        if href:
            a.click()
            self.set_code()

    def set_code(self):
        # 1.切换句柄
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[1])

        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')

        self.del_mysql()

        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            # print(code,name)
            if code.endswith('0000'):
                self.province.append((name,code))
                if name in ("北京市","天津市","上海市","重庆市"):
                    self.city.append((name,code,code))
            elif code.endswith('00'):
                self.city.append((name,code,code[:2]+'0000'))
            else:
                if code[:2] in ("11","12","31","50"):
                    self.county.append((name,code,code[:2]+'0000'))
                else:
                    self.county.append((name,code,code[:4]+'00'))
        print("数据抓取完成")
        self.save_mysql()
        print("数据保存完成")

    def del_mysql(self):
        sql = "delete from province"
        self.cursor.execute(sql)
        sql = "delete from city"
        self.cursor.execute(sql)
        sql = "delete from county"
        self.cursor.execute(sql)
        self.db.commit()

    def save_mysql(self):
        sql = "insert into province(p_name,p_code) values (%s,%s)"
        self.cursor.executemany(sql,self.province)
        sql = "insert into city(c_name,c_code,c_father_code) values (%s,%s,%s)"
        self.cursor.executemany(sql, self.city)
        sql = "insert into county(x_name,x_code,x_father_code) values (%s,%s,%s)"
        self.cursor.executemany(sql, self.county)
        self.db.commit()

gs = GovSpider()
gs.get_data()
```



### 10.execjs模块

```shell
# 下载 
sudo pip3 install pyexecjs
```

```python
# 获取 JS 代码中的返回值
import execjs

with open('translate.js','r') as f:
    js_data = f.read()

exec_obj = execjs.compile(js_data)
result = exec_obj.eval('e("hell")')
print(result)
```

### 11.scrapy 框架

####     1.安装

```shell
# Ubuntu安装
1、安装依赖包
	1、sudo apt-get install libffi-dev
	2、sudo apt-get install libssl-dev
	3、sudo apt-get install libxml2-dev
	4、sudo apt-get install python3-dev
	5、sudo apt-get install libxslt1-dev
	6、sudo apt-get install zlib1g-dev
	7、sudo pip3 install -I -U service_identity
2、安装scrapy框架
	1、sudo pip3 install Scrapy
```

```shell
# Windows安装
cmd命令行(管理员): python -m pip install Scrapy
# Error: Microsoft Visual C++ 14.0 is required xxx
```

####     2.命令

```shell
# 创建一个 Baidu 的项目
scrapy startproject Baidu
# 创建爬虫文件
scrapy genspider 爬虫名 域名
# 运行爬虫文件
scrapy crawl 爬虫名
```

####     3.scrapy项目结构

```shell
Baidu                   # 项目文件夹
├── Baidu               # 项目目录
│   ├── items.py        # 定义数据结构
│   ├── middlewares.py  # 中间件
│   ├── pipelines.py    # 数据处理
│   ├── settings.py     # 全局配置
│   └── spiders
│       ├── baidu.py    # 爬虫文件
└── scrapy.cfg          # 项目基本配置文件
```

####     4.案例

### 12.下载大文件

```python
# 设置 stream = True
# iter_content：一块一块的遍历要下载的内容
# iter_lines：一行一行的遍历要下载的内容
url = http://.../test01.zip"
with open(d_filename, 'wb') as f:
    with requests.get(url=url,stream = True) as res:
        # siza_all = res.headers.get("Content-Length")  显示下载百分比时使用
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
```



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