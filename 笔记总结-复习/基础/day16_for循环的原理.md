### for循环的原理
    (1)获取迭代器
    (2)循环获取下一个元素
    (3)遇到异常停止

```
list_ = ["张三丰","张翠山","张无忌"]
for item in list_:
    print(item)

#for循环的原理
listiter =list_.__iter__() #获取迭代器
while True:
    try:
        item = listiter.__next__() #循环获取下一个元素
        print(item)
    except StopIteration:
        break
```
