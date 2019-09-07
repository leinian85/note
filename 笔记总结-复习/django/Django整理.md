# Django 框架设计



## 目录

[TOC]

## Django的官网

- 官方网址: <http://www.djangoproject.com>
- 中文文档(第三方):
  - <https://yiyibooks.cn/>
  - <http://djangobook.py3k.cn/>

## Django的安装

- 查看已安装的版本

  ```python
  >>> import django
  >>> print(django.VERSION)
  (1, 11, 8, 'final', 0)
  ```

- 在线安装

  ```shell
  # 安装django的最新版本
  $ sudo pip3 install django
  #安装django的指定版本
  $ sudo pip3 install django[==版本]
  # 如:
  $ sudo pip3 install django==1.11.8
  ```

- Django的卸载

  ```shell
  $ pip3 uninstall django
  ```

- Django 的开发环境

  - Django 1.11.x 支持 Python 2.7, 3.4, 3.5 和 3.6（长期支持版本 LTS)
  - 注: Django 1.11.x 不支持 Python 3.7


## Django 使用/命令

```shell
# 1.创建一个 Django 项目,名称为 store
$ django-admin startproject store
# 2.启动服务
$ cd store
$ python3 manage.py runserver
# 或
$ python3 manage.py runserver 5000  # 指定只能本机使用127.0.0.1的5000端口访问本机

# 创建一个应用,名称为 book
$ python3 manage.py startapp book
# 创建模板目录
$ mkdir templates
```

## Django 配置

#### 配置语言,时间

- settings.py 设置中文 / 时间

  ```shell
  # LANGUAGE_CODE = 'en-us'
  LANGUAGE_CODE = 'zh-Hans'
  
  # TIME_ZONE = 'UTC'
  TIME_ZONE = 'Asia/Shanghai'
  ```

#### 配置模板

- settings.py 设置模板路径 

  **设置 TEMPLATES 下的 DIRS 为 os.path.join(BASE_DIR,'templates')**

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR,'templates')],
          'APP_DIRS': True,
      },
  ]
  ```

#### 配置应用以及路由

- settings.py 添加应用模块 book

  ```
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'book',
  ]
  ```

  

- urls.py 设置主路由的

  ```python
  from django.conf.urls import include
  
  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^book/', include('book.urls')),
  ]
  ```

- 创建并设置分路由

  在`book`下创建文件`urls.py` 

  ```python
  # 配置分路由 urls.py
  from django.conf.urls import url
  from . import views
  
  urlpatterns = [
      url(r'^$', views.index),
  ]
  ```

#### 配置路由对应的视图文件

- 修改 `book/views.py` 文件,增加视图函数

  ```python
  from django.shortcuts import render
  
  def index(request):
      if request.method == "GET":
          return render(request,"book/index.html")
  ```

#### 配置视图文件对应的模板文件

- 在`book`下创建目录`templates`并在`templates`中创建`book`目录, 用于存放`book`应用的模板

  在`book`下创建 `index.html`文件,后面的页面需要继承 index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      {% block title %}
      <title>首页</title>
      {% endblock%}
  </head>
  <body>
      <a href="/book/add_book">添加书籍</a>
      <a href="/book/sel_book">查看书籍</a>
      {% block body %}
      {% endblock body %}
  </body>
  </html>
  ```

#### 配置数据库后台

- settings.py 配置数据库

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'store',
          'HOST':'127.0.0.1',
          'PORT':'3306',
          'USER':'root',
          'PASSWORD':'123456'
      }
  }
  ```

  `store/__init__.py` 修改代码:

  ```python
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

- models.py 配置数据库模型

  ```python
  from django.db import models
  
  class Author(models.Model):
      name = models.CharField(max_length=40, verbose_name="姓名")
      sex = models.IntegerField(null=True, verbose_name="性别")
      age = models.IntegerField(null=True, verbose_name="年龄")
  
      # 下面的代码是为了在后台操作外键关联的时候可以显示在界面上
      def __str__(self):
          return self.name
  	
  class Pub(models.Model):
      name = models.CharField(max_length=100, verbose_name="出版社名称")
  
      # 下面的代码是为了在后台操作外键关联的时候可以显示在界面上
      def __str__(self):
          return self.name
  
  class Book(models.Model):
      title = models.CharField(max_length=100, verbose_name="书名")
      author = models.ForeignKey(Author,null=True) # 外键
      pub = models.ForeignKey(Pub,null=True)   # 外键
  ```

  

- 注册数据库表:

  ```shell
  $ python3 manage.py makemigrations
  $ python3 manage.py migrate
  ```

  

- 配置数据库表在后台展示

  创建超级用户:

  ```shell
  $ python3 manage.py createsuperuser
  ```

  在浏览器中输入:127.0.0.1:8000/admin 就可以登录管理

  

- book/admin.py 配置可以在后台管理的表

  ```python
  from django.contrib import admin
  from . import models
  
  class AuthorManage(admin.ModelAdmin):
      list_display = ["name", "sex", "age"]
  
  class PubManage(admin.ModelAdmin):
      list_display = ["name"]
  
  class BookManage(admin.ModelAdmin):
      # 此处的外键 author,pub 会显示对应的类中的 __str__ 方法返回的值
      list_display = ["title", "author", "pub"]
      list_editable = ["pub"]  # 可编辑字段
      list_filter = ["pub"]   # 过滤
  
  admin.site.register(models.Author, AuthorManage)
admin.site.register(models.Pub, PubManage)
  admin.site.register(models.Book, BookManage)
  ```
  
  

#### 静态文件

- 在`book`下创建目录`static`用于存放静态文件

- 在`static`下增加相应的目录存放相应的文件,如添加 css  js  imgs 目录存放css文件,js文件和图片

- `settings.py`配置静态文件路径:

  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = (
      os.path.join(BASE_DIR,"static"),
      os.path.join(BASE_DIR,"book/static"),
  )
  ```



## 数据库操作(以book应用为例)

#### 关闭中间件

- setting.py

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 屏蔽此段,否则 post 请求不通过
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```



#### 路由文件配置

- book/urls.py

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$',views.add_book),
    url(r'^sel_book$',views.sel_book),
    url(r'^update_book$',views.update_book),
    url(r'^del_book$',views.del_book),
]
```

#### 首页

- 首页只有新增和查询功能,该功能被增加,修改,查询继承

- 页面 : index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      {% block title %}
      <title>首页</title>
      {% endblock%}
  </head>
  <body>
      <a href="/book/add_book">添加书籍</a>
      <a href="/book/sel_book">查看书籍</a>
      {% block body %}
      {% endblock body %}
  </body>
  </html>
  ```

  

#### 增加 

- book/views.py 的 add_book 函数(代码在后面)

- 页面 : add.html 代码:

  ```html
  {% extends "book/index.html" %}
  {% block title %}
  <title>新增书籍</title>
  {% endblock%}
  {% block body %}
  {{ book }}
  <form action="{% if book %}/book/update_book
                {% else %}/book/add_book
                {% endif %}"
        method="post">
      <input type="text" hidden name = "id" value={{ book.id }}>
      <div>
          书名: <input type="text" name="title" value="{{ book.title }}">
      </div>
  
      {% if pubs is not null %}
      <div>出版社:
          <select name="pub_id">
              {% for pub in pubs %}
              <option value="{{ pub.id }}"
                      {% if book.pub_id == pub.id %}selected{% endif %}>
                  {{ pub.name }}
              </option>
              {% endfor %}
          </select>
      </div>
      {% endif %}
  
      {% if authors is not null %}
      <div>作者:
          <select name="author_id">
              {% for author in authors %}
              <option value="{{ author.id }}"
                      {% if book.author_id == author.id %}selected{% endif %}>
                  {{ author.name }}
              </option>
              {% endfor %}
        </select>
      </div>
      {% endif %}
      <input type="submit" value="{% if book %}修改{% else %}增加{% endif %}">
  </form>
  {{ msg }}
  {% endblock body %}
  ```
  
  

#### 修改

- book/views.py  的 update_book 函数(代码在后面)
- 页面 : 修改页面与增加页面公用

#### 删除

- book/views.py 的 del_book 函数(代码在后面)
- 页面 : 删除功能无页面

#### 查询

- book/views.py 的 sel_book 函数(代码在后面)

- 页面 : sel_book.html

  ```html
  {% extends "book/index.html" %}
  {% block body %}
  <table>
      <tr>
          <td>书名</td>
          <td>作者</td>
          <td>出版社</td>
          <td>修改</td>
          <td>删除</td>
      </tr>
      {% for book in books %}
      <tr>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.pub }}</td>
          <td><a href="/book/add_book?id={{ book.id }}">修改</a></td>
          <td><a href="/book/del_book?id={{ book.id }}">删除</a></td>
      </tr>
      {% endfor %}
  </table>
  {% endblock body%}
  ```

  

#### book/viewspy

```python
from django.shortcuts import render
from . import models

def index(request):
    if request.method == "GET":
        return render(request,"book/index.html")

def add_book(request):
    pubs = models.Pub.objects.all()
    authors = models.Author.objects.all()
    if request.method == "GET":
        try:
            book = models.Book.objects.get(id = request.GET.get("id"))
        except:
            book = None
    elif request.method =="POST":
        try:
            title = request.POST.get("title")
            pub_id = request.POST.get("pub_id")
            author_id = request.POST.get("author_id")
            models.Book.objects.create(title = title,
                                       pub_id = pub_id,
                                       author_id = author_id)
            msg = "添加成功!"
        except Exception as e:
            msg = e
    return render(request, "book/add.html", locals())


def sel_book(request):
    books = models.Book.objects.all()
    return render(request,"book/sel_book.html",locals())

def update_book(request):
    if request.method == "POST":
        try:
            book = models.Book.objects.get(id = request.POST.get("id"))
            book.title = request.POST.get("title")
            book.author_id = request.POST.get("author_id")
            book.pub_id = request.POST.get("pub_id")
            book.save()
            msg = "修改成功"
            book = None
            pubs = models.Pub.objects.all()
            authors = models.Author.objects.all()
        except Exception as e:
            msg = e
    return render(request,"book/add.html",locals())


def del_book(request):
    if request.method == "GET":
        id = request.GET.get("id")
        book = models.Book.objects.get(id = id)
        book.delete()
    books = models.Book.objects.all()
    return render(request,"book/sel_book.html",locals())
```



## Django使用的命令汇总

```shell
# 1.创建一个 Django 项目,名称为 store
$ django-admin startproject store

# 2.启动服务
$ python3 manage.py runserver
# 或
$ python3 manage.py runserver 5000  # 指定只能本机使用127.0.0.1的5000端口访问本机

# 3.创建一个应用,名称为 book
$ python3 manage.py startapp book

# 4.注册数据库(将表添加到数据库)
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# 5.创建超级用户(后台管理数据库表)
$ python3 manage.py createsuperuser
```



## 登录功能

#### 创建数据库

```sql
mysql> create database blog charset utf8;
```

#### 添加 blog 应用

```shell
$ python3 manage.py startapp blog
```

#### 配置

```

```





