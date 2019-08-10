# 题目006：斐波那契数列。
# 斐波那契数列，又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


def num_n(n):
    if n == 2 or n == 3:
        return 1

    return num_n(n-1)+num_n(n-2)


print(num_n(7))