[TOC]
### 数据库分类
- 关系型
- 非关系型

### 关系型数据库组织结构
数据元素 --> 记录 --> 数据表 --> 数据库
数据库(database)
数据表(table)
记录(row)
字段(column)
主键:不能重复能为空(primary key)

### mysql
mysql安装,配置

#### mysql基本操作

##### 1.创建数据库
```sql
e.g. 创建stu数据库，编码为utf8
create database stu character set utf8;
create database stu charset=utf8;
use stu   # 切换到stu库
```

##### 2.创建表 
```sql
create table users(
    id         int auto_increment primary key,
    login_name varchar(32) not null,
    password   varchar(10) default '123456',
    sex        enum('M','F'),
    weight     decimal(6,2) unsigned,
    level      char,
    remark     text,
    image      longblob
);
```
```
(1)字段描述:
primary key 主键
unsigned 无符号
not null
default
auto_increment 自增
```
```
(2)数据类型:
#数字: 
    int | float | double | decimal
    DECIMAL(6,2)最多存6位数字，小数点后占2位
#字符串:
    char | varchar | blob | text | enum | set
    text 和 blob
    text 用来存储非二进制文本
    blob 用来存储二进制字节串
#日期:
    date ："YYYY-MM-DD"
    time ："HH:MM:SS"
    datetime ："YYYY-MM-DD HH:MM:SS"
    timestamp ："YYYY-MM-DD HH:MM:SS"
    datetime ：不给值默认返回NULL值
    timestamp ：不给值默认返回系统当前时间
```

##### 3.表字段结构修改
```sql
语法 ：alter table 表名 执行动作;
alter table tablename add 
                      drop 
                      modify
                      change
                      rename

* 添加字段(add)
    alter table 表名 add 字段名 数据类型;
    alter table 表名 add 字段名 数据类型 first;
    alter table 表名 add 字段名 数据类型 after 字段名;
* 删除字段(drop)
    alter table 表名 drop 字段名;
* 修改数据类型(modify)
    alter table 表名 modify 字段名 新数据类型;
* 修改字段名(change)
    alter table 表名 change 旧字段名 新字段名 新数据类型;
* 表重命名(rename)
    alter table 表名 rename 新表名;
```
##### 4.时间格式
    now() 返回服务器当前时间
    curdate() 返回当前日期
    curtime() 返回当前时间
    date(date) 返回指定时间的日期
    time(date) 返回指定时间的时间
```sql
mysql> select now(),curdate(),curtime();
+---------------------+------------+-----------+
| now()               | curdate()  | curtime() |
+---------------------+------------+-----------+
| 2019-07-17 19:46:15 | 2019-07-17 | 19:46:15  |
+---------------------+------------+-----------+


mysql> select * from marathon;
+----+--------+---------------------+----------+
| id | name   | enter_time          | croce    |
+----+--------+---------------------+----------+
|  1 | 赵四   | 2019-05-18 12:00:00 | 02:30:30 |
+----+--------+---------------------+----------+

mysql> select date(enter_time),time(enter_time) from marathon;
+------------------+------------------+
| date(enter_time) | time(enter_time) |
+------------------+------------------+
| 2019-05-18       | 12:00:00         |
+------------------+------------------+
```

##### 5.日期时间运算
    时间间隔单位： year | month | day | hour | minute 
```sql
mysql> select now() - interval 1 year;
+-------------------------+
| now() - interval 1 year |
+-------------------------+
| 2018-07-17 19:49:45     |
+-------------------------+

mysql> select curtime() - interval 10 minute;
+--------------------------------+
| curtime() - interval 10 minute |
+--------------------------------+
| 19:40:11                       |
+--------------------------------+
```

##### 6.正则匹配 REGEXP

##### 7.分页/限制 LIMIT
```sql
#取成绩前3名
mysql> select * from class order by score desc limit 3;
+----+-----------+-----+------+-------+--------------+
| id | name      | age | sex  | score | 入学时间     |
+----+-----------+-----+------+-------+--------------+
|  1 | 张无忌    |  23 | 男   |   100 | 2019-05-31   |
|  4 | 张三      | 108 | 男   |    99 | 2019-05-31   |
|  2 | 赵敏      |  21 | 女   |    98 | 2015-05-06   |
+----+-----------+-----+------+-------+--------------+
```

#### mysql备份,恢复
(1).备份
```
#将目标库导出到文件stu.sql(不指定路径就是当前文件夹)
mysqldump -uroot -p 目标库 > stu.sql

    库名 备份单个库
    --all-databases 备份所有库
    -B 库1 库2 库3 备份多个库
    库名 表1 表2 表3 备份指定库的多张表
```
(2).恢复
```
#将stu.sql文件导入到目标库
mysql -uroot -p 目标库 < stu.sql
#(注意):目标库必须存在,如果不存在就需要先创建
```

#### mysql主从复制


#### 新安装的mysql设置密码
```sql
use mysql;
update user set password=PASSWORD('root') where user='root';
flush privileges;
```

#### mysql不能被远程访问的原因(3个原因):
    1.网络/防火墙:(远程服务器的IP:192.168.80.130)
```shell
ping 192.168.80.130  # 如果不通就是网络的问题
telnet 192.168.80.130 3306 #如果不通,就是mysql的服务器防火墙没有开放3306端口
    
处理方法(centos7):
开放3306端口命令：
firewall-cmd --zone=public --add-port=3306/tcp --permanent
重启防火墙：
systemctl restart firewalld.service
命令含义：
--zone #作用域
--add-port=3306/tcp  #添加端口，格式为：端口/通讯协议
--permanent   #永久生效，没有此参数重启后失效

防火墙的设置:
(1).开启防火墙，
启动firewall：
systemctl start firewalld.service
(2).设置开机自启：
systemctl enable firewalld.service
(3).重启防火墙：
systemctl restart firewalld.service
(4)检查防火墙状态是否打开：
firewall-cmd --state
```
    2.mysql的配置文件的问题
```
(1)检查MySQL配置,查看3306端口状态
netstat -apn|grep 3306
tcp6  0  0 127.0.0.1:3306  :::*  LISTEN    13524/mysqld
(2)检查my.cnf的配置文件，bind-address=addr可以配置绑定ip地址。
不配置或者IP配置为0.0.0.0，表示监听所有客户端连接。
找到配置文件并屏蔽 bind-address 配置文件可能比较难找
```
```sql
#用下面的语句也可以查看mysql的端口
mysql> show global variables like 'port';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| port          | 3306  |
+---------------+-------+
```
    3.mysql的密码设置问题
```sql
#切换到mysql数据库:
user mysql;
#将数据库 stu 授权可以远程访问:
GRANT ALL PRIVILEGES ON stu.* TO mysql@'%' IDENTIFIED BY '123456' WITH GRANT OPTION; 
#刷新
FLUSH PRIVILEGES;

mysql> select host,user,authentication_string from user;
+-----------+------------------+-------------------------------------------+
| host      | user             | authentication_string                     |
+-----------+------------------+-------------------------------------------+
| localhost | root             | *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9 |
| localhost | mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| localhost | mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| localhost | debian-sys-maint | *D64249D961AE43EAD3B8B30EAE0A2938F892048F |
| %         | mysql            | *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9 |
+-----------+------------------+-------------------------------------------+

```