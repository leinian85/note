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