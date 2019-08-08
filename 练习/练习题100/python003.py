# 题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# 解法一:
def get_num():
    for i in range(100001):
        for n in range(101):
            if n ** 2 == (i +100):
                for m in range(101):
                    if m **2 == (i+168):
                        print(i,n,m)

# 解法二:
def get_num2():
    _list = []
    for i in range(101):
        _list.append(i**2)

    for i in range(len(_list)-1):
        for n in range(i+1,len(_list)):
            if _list[n] - _list[i] == 68:
                print(_list[i],_list[n],_list[i]-100,_list[n]-168)


# get_num();
get_num2();