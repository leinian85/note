MYSQL
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

### mysql安装
    mysql安装,配置

##### 新安装的mysql设置密码
```sql
use mysql;
update user set password=PASSWORD('root') where user='root';
flush privileges;
```

### mysql基本操作
##### 1.数据库管理
```sql
# 1.查看已有库
show databases;
# 2.创建数据库并指定数据集为utf8
create database 库名 charset utf8;
create database 库名 charset=utf8;
create database 库名 character set utf8;
# 3.查询当前所在库
select database();
# 4.切换库
use 库名
# 5.删除库
drop database 库名;
```
##### 2.表的管理
```sql
# 1.创建表并指定字符集
create table 表名(字段名 字段类型 XXX,);
create table users(
    id         int auto_increment primary key,
    login_name varchar(32) not null,
    password   varchar(10) default '123456',
    sex        enum('M','F'),
    weight     decimal(6,2) unsigned,
    level      char,
    phone      int,
    remark     text,
    image      longblob,
    index(login_name),
    unique(phone)
);
charset=utf8;
# 2.查看创建表的语句(字符集,存储引擎)
show create table 表名;
# 3.查看表结构
desc 表名;
# 4.删除表
drop table 表名1,表名2,表名3
```

##### 3.表字段管理
```sql
# 语法 ：alter table 表名 执行动作;
alter table tablename add 
                      drop 
                      modify
                      change
                      rename

# 添加字段(add)
alter table 表名 add 字段名 数据类型;
alter table 表名 add 字段名 数据类型 first;
alter table 表名 add 字段名 数据类型 after 字段名;
# 删除字段(drop)
alter table 表名 drop 字段名;
# 修改数据类型(modify)
alter table 表名 modify 字段名 新数据类型;
# 修改字段名(change)
alter table 表名 change 旧字段名 新字段名 新数据类型;
# 表重命名(rename)
alter table 表名 rename 新表名;
```

##### 4.表字段描述,数据类型
```sql
(1)字段描述:
primary key 主键
unsigned 无符号
not null
default
auto_increment 自增

(2)数据类型:
# 数字: 
    int | smallint | bigint | tinyint[1]
    float(m,n) | double | decimal
    DECIMAL(6,2)最多存6位数字，小数点后占2位
# 字符串:
    char 数据长度不足用空格来补 
    varchar 补位:会额外增加长度来存储实际长度 
    blob | text | 
    text 和 blob
    text 用来存储非二进制文本
    blob 用来存储二进制字节串
# 枚举
    enum 只能单选 
    set  可以多选
# 日期:
    year : "YYYY"
    date ："YYYY-MM-DD"
    time ："HH:MM:SS"
    datetime ："YYYY-MM-DD HH:MM:SS"
    timestamp ："YYYY-MM-DD HH:MM:SS"
    datetime ：不给值默认返回NULL值
    timestamp ：不给值默认返回系统当前时间
```

##### 5.时间函数
```sql
now() 返回服务器当前时间
curdate() 返回当前日期
curtime() 返回当前时间
year(字段名)
date(字段名)
time(字段名)
date(date) 返回指定时间的日期
time(date) 返回指定时间的时间

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

##### 6.日期时间运算
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

### 索引
```sql
# 创建索引
create index 索引名 on 表名(字段名);
```
    B-Tree 的特点:
    1.全部节点均包含 索引(键值) + 数据
    2.范围查询 从根节点遍历至指定数据

    B+Tree的特点:
    1.非叶子节点只存储 索引(键值) 信息(树的深度都优于B树,从而降低了磁盘IO)
    2.叶子节点均包含 索引(id) + 数据(卫星数据)
    3.每个父节点都出现在子节点中,是子节点最大或最小的元素.
    4.叶子节点包含了所有元素.
    5.所有叶子节点之间都有一个链指针,形成链表结构
    6.范围查询 在叶子节点找到数据后直接从叶子节点遍历

    B+Tree对于BTree的优势:
    1.单一节点存储更多的元素（这样该节点下分支变多了，树变矮胖了），使得查询的IO次数更少。
    2.所有查询都要查找到叶子节点，查询性能稳定。
    3.所有叶子节点形成有序链表，便于范围查询。

>数据库中的B+Tree索引可以分为聚集索引（clustered index）和辅助索引（secondary index）。上面的B+Tree示例图在数据库中的实现即为聚集索引，聚集索引的B+Tree中的叶子节点存放的是整张表的行记录数据。辅助索引与聚集索引的区别在于辅助索引的叶子节点并不包含行记录的全部数据，而是存储相应行数据的聚集索引键，即主键。当通过辅助索引来查询数据时，InnoDB存储引擎会遍历辅助索引找到主键，然后再通过主键在聚集索引中找到完整的行记录数据。

![BTree]("mysql/BTree.png" "BTree")
![B+Tree]("mysql/B+Tree.png" "B+Tree")

### 搜索引擎
mysql主要有2种搜索引擎:Innodb / MyIsam


### 正则匹配 REGEXP


### mysql备份,恢复 .sql
(1).备份
```
#将目标库导出到文件stu.sql(不指定路径就是当前文件夹)
mysqldump -uroot -p 目标库 > 导出文件路径

    库名 备份单个库
    --all-databases 备份所有库
    -B 库1 库2 库3 备份多个库
    库名 表1 表2 表3 备份指定库的多张表
```
(2).恢复
```
# 将sanguo.sql文件导入到目标库
# (注意):目标库必须存在,如果不存在就需要先创建
# 方法一:
mysql -uroot -p 目标库 < /home/tarena/1905/gittarena/sanguo.sql

# 方法二:
mysql> source /home/tarena/1905/gittarena/sanguo.sql
```

### mysql备份,恢复 .cvs/.txt/...
    导出语法:
```sql
select ... from 表名
into outfile "文件名"
fields terminated by "分隔符"
lines terminated by "分隔符";

# 导出的路径必须是当前数据库下的路径 如: /var/lib/mysql-files/
eg.
mysql> select * from sanguo
    -> into outfile "/var/lib/mysql-files/sanguo.csv"                        
    -> fields terminated by ","                                                     
    -> lines terminated by "\n";
```
    导入语法:
```sql
load data infile "文件名"
into table 表名
fields terminated by "分隔符"
lines terminated by "\n";

# 导入前先将文件放到mysql的查找路径中
mysql> show variables like 'secure_file_priv';
+------------------+-----------------------+
| Variable_name    | Value                 |
+------------------+-----------------------+
| secure_file_priv | /var/lib/mysql-files/ |
+------------------+-----------------------+

sodu cp /home/tarena/sanguo.csv  /var/lib/mysql-files/

eg.
mysql> load data infile "/var/lib/mysql-files/sanguo.csv"
    -> into table sanguo
    -> fields terminated by ","
    -> lines terminated by "\n";

```

### mysql主从复制


### mysql不能被远程访问的原因(3个原因):
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