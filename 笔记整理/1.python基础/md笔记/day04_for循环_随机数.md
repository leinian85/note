[TOC]
### 1.循环语句：
```
for 变量 in 可迭代对象:
    循环体
```

### 2.整数迭代器
>range(0,6) 可以迭代出0到6的整数，含头不含尾

### 3.随机函数 random
>import random
random.randInt(1,100) # 随机产生1到100之间的整数，包含1和100

### 4.字节，字符集
>ord() 将字符转换秤编码  # 字－－> 数
chr() 将编码转换秤字符  # 数－－> 字
![字符集](../day04/字符集.jpg "字符集")

### 5.转义符
>print(r"\n123")
\

### 6.格式化输出
>print(“我叫%s,年龄是%d,成绩是%.2f” %(name,age,score))
list01 = [1,2,3,4,5]
print("".join("%d"%item for item in list01))


