### 1.string

```shell
1、查看 db0 库中所有的键 

2、设置键 trill:username 对应的值为 user001，并查看 

3、获取 trill:username 值的⻓度 

4、一次性设置 trill:password 、trill:gender、trill:fansnumber 并查看

5、查看键 trill:score 是否存在

6、增加10个粉丝

7、增加2个粉丝(一个一个加) 

8、有3个粉丝取消关注你了

9、又有1个粉丝取消关注你了

10、思考、思考、思考...,清除当前库

11、一万个思考之后，清除所有库 

```

### 2.list

```shell
1、查看所有的键

2、向列表 spider:urls 中以RPUSH放入如下几个元素:01_baidu.com、02_taobao.com、 03_sina.com、04_jd.com、05_xxx.com

3、查看列表中所有元素

4、查看列表⻓度

5、将列表中01_baidu.com 改为 01_tmall.com 

6、在列表中04_jd.com之后再加1个元素 02_taobao.com

7、弹出列表中的最后一个元素

8、删除列表中所有的 02_taobao.com

9、剔除列表中的其他元素，只剩前3条

```



### 3.set

### 练习题：

```python
一、网易音乐排行榜 - Python
1、每首歌的歌名作为元素 
2、每首歌的播放次数作为分值 
3、使用ZREVRANGE来获取播放次数最多的歌曲

二、 京东商品畅销榜 - Python
# 第1天
ZADD mobile-001 5000 'huawei' 4000 'oppo' 3000 'iphone'
# 第2天
ZADD mobile-002 5200 'huawei' 4300 'oppo' 3230 'iphone'
# 第3天
ZADD mobile-003 5500 'huawei' 4660 'oppo' 3580 'iphone' 问题:如何获取三款收集的销量排名?
ZUNIONSTORE mobile-001:003 3 mobile-001 mobile-002 mobile-003 # 可否?
```

