# 题目005：输入三个整数x, y, z，请把这三个数由小到大输出。

def short(*args):
    _list = list(args)
    for i in range(len(_list)-1):
        for j in range(i+1,len(_list)):
            if _list[i] > _list[j]:
                _list[i],_list[j] = _list[j],_list[i]

    for item in _list:
        print(item,end=" ")

short(3,5,2)