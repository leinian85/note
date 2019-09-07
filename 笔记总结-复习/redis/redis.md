[TOC]



### redis

#### 数据类型:

##### 1.字符串

```R
SET | GET | MSET | MGET
```

##### 2.列表

```R
LPUSH | RPUSH | LPOP | RPOP | BLPOP | BRPOP | LLEN | LTRIM
```

##### 3.集合

```R
SADD | SMEMBERS | SPOP | SINTER | SUNION
```

##### 4.有序集合

```
ZADD | ZREVRANGE | ZRANGE
```

##### 5.hash(散列)

```R
HSET | HGET | HMSET | HMGET | HGETALL | HKEYS | HINCRBY
```

字符串类型与hash类型对比:

字符串类型:

| key            | value |
| -------------- | ----- |
| user001:name   | Lucy  |
| user001:age    | 25    |
| user001:gender | F     |

hash类型:

| key     | filed  | value |
| ------- | ------ | ----- |
| user001 | name   | Lucy  |
|         | age    | 25    |
|         | gender | F     |

基本操作:

```python
import redis
r = redis.Redis(host="leinian",port=6379,db=0)

# hset hget
r.hset("user001","name","Lucy")
name = r.hget("user001","name")
print(name) # b'Lucy'

# hmset hmget
user = {
    "name":"Lucy",
    "age":25,
    "gender":"F"
}
r.hmset("user001",user)
user = r.hmget("user001","name","age","gender")
print(user) # [b'Lucy', b'25', b'F']

# hgetall hkeys hvals
user001 = r.hgetall("user001")
print(user001) # {b'name': b'Lucy', b'age': b'25', b'gender': b'F'}

keys = r.hkeys("user001")
print(keys) # [b'name', b'age', b'gender']

vals = r.hvals("user001")
print(vals) # [b'Lucy', b'25', b'F']

# hdel
r.hdel("user001","gender","age")
print(r.hgetall("user001"))
```

使用场景 : 

1.获取用户信息

先从redis里面取用户数据,没有就从mysql中取,取到之后缓存到redis中

2.更新用户信息

先更新mysql中的信息,再更新redis里面的信息

```python
# redis+hash+mysql组合使用
import redis
import pymysql
import hashlib

class UserEdit:
    def __init__(self):
        self.r = redis.Redis(host="leinian", port=6379, db=0)
        self.db = pymysql.connect(
            host="leinian",
            user="root",
            password="123456",
            port=3306,
            charset="utf8",
            database="blog"
        )
        self.cursor = self.db.cursor()

    # 获取用户信息并缓存到redis中
    def get_userinfo(self,username):
        sql = "select username,password,email from user where username = %s"
        self.cursor.execute(sql, [username])
        userinfo = self.cursor.fetchone()

        if userinfo:
            userinfo_dict = {
                "username": userinfo[0],
                "password": userinfo[1],
                "email": userinfo[2]
            }

            self.update_redis(username, userinfo_dict)
            return userinfo_dict
        else:
            return None

    # 更新数据到 redis 中
    def update_redis(self,username,userinfo):
        self.r.hmset(username,userinfo)
        self.r.expire(username, 30)

    # 打印用户信息
    def print_userinfo(self,username):
        userinfo = self.r.hgetall(username)
        if userinfo:
            for key in userinfo:
                print(key.decode(), self.r.hget(username, key).decode())
        else:
            userinfo = self.get_userinfo(username)

            if userinfo:
                for k in userinfo:
                    print("%s:%s" % (k, userinfo[k]))
            else:
                print("用户不存在")

    # 更新用户信息
    def update_info(self,username,password,email):
        hs = hashlib.md5()
        hs.update(password.encode())
        pwd = hs.hexdigest()

        try:
            sql = "update user set password = %s,email=%s where username = %s"
            self.cursor.execute(sql,[pwd,email,username])
            self.db.commit()
        except:
            self.db.rollback()
            print("更改失败")
            return
        userinfo={
            "username":username,
            "password":pwd,
            "email":email
        }
        self.update_redis(username,userinfo)
        print("更新成功")

if __name__ == "__main__":
    UE = UserEdit()
    username = "leinian"
    UE.update_info(username,'123456','42737521@qq.com')
    UE.print_userinfo(username)
```





#### 位图操作:

**==位图操作实际上是对字符串的操作==**

##### 命令行操作:

```shell
# 设置user001的第0位为1
setbit user001 0 1
# 取出user001的第0位
getbit user001 0
# 计算user001中有多少个1
# [start end]代表的是字节数,不是位数,下面是取出user001中前8位有多少个1
bitcount user001 0 0
```



##### python操作:

```python
"""位图操作寻找活跃用户"""
import redis

r = redis.Redis(host="leinian",port=6379,db=0)

#user:001 一年中第5天和第200天登录
r.setbit("user:001",4,1)
r.setbit("user:001",199,1)


#user:002 一年中第100天和第300天登录
r.setbit("user:002",99,1)
r.setbit("user:002",299,1)


#user:003 一年中登录了100次以上
for i in range(5,108):
    r.setbit("user:003",i,1)

#user:004 一年中登录了100次以上
for i in range(150):
    r.setbit("user:004",i,1)

# 取出用户的活跃天数
keys = r.keys("user:*")
active = []
noactive = []
for keyb in keys:
    key = keyb.decode()
    count = r.bitcount(key)
    user = (key,count)
    if count > 100:
        active.append(user)
    else:
        noactive.append(user)

print(active)
print(noactive)
```

redis持久化

1.RDB

```shell
SAVE | BGSAVE
# aof持久化开启
appendonly yes
appendfilename 'appendonly.aof'
```

2.AOF

```shell
# aof持久化策略
appendfsync always          # 每条语句保存一次
appendfsync everysec # 默认    每隔一秒保存一次
appendfsync no              # 系统自己保存
```



redis常用配置总结:

```shell
# 设置密码
1、requirepass password
# 开启远程连接
2、bind 127.0.0.1 ::1 注释掉
3、protected-mode no  把默认的 yes 改为 no
# rdb持久化-默认配置
4、dbfilename 'dump.rdb'
5、dir /var/lib/redis
# rdb持久化-自动触发(条件)
6、save 900 1
7、save 300 10 
8、save 60  10000
# aof持久化开启
9、appendonly yes
10、appendfilename 'appendonly.aof'
# aof持久化策略
11、appendfsync always
12、appendfsync everysec # 默认
13、appendfsync no
# aof重写触发
14、auto-aof-rewrite-percentage 100
15、auto-aof-rewrite-min-size 64mb
# 设置为从服务器
16、salveof <master-ip> <master-port>
```

Redis相关文件存放路径

```shell
1、配置文件: /etc/redis/redis.conf
2、备份文件: /var/lib/redis/*.rdb|*.aof
3、日志文件: /var/log/redis/redis-server.log
4、启动文件: /etc/init.d/redis-server
# /etc/下存放配置文件
# /etc/init.d/下存放服务启动文件
```

