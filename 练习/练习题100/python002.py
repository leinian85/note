"""
题目002：企业发放的奖金根据利润(I)的多少来提成：
低于或等于10万元时，奖金可提10 %；
利润高于10万元，低于20万元时，低于10万元的部分按10 % 提成，高于10万元的部分，可提成7.5 %；
20万到40万之间时，高于20万元的部分，可提成5 %；
40万到60万之间时高于40万元的部分，可提成3 %；
60万到100万之间时，高于60万元的部分，可提成1.5 %；
高于100万元时，超过100万元的部分按1 % 提成。
从键盘输入当月利润I，求应发放奖金总数？
"""


# 解法一:
def get_money(money):
    min = 100000 if money > 100000 else money
    sum1 = min * 10 / 100
    min = 200000 - 100000 if money > 200000 else money - 100000
    sum2 = (min if min > 0 else 0) * 7.5 / 100
    min = 400000 - 200000 if money > 400000 else money - 200000
    sum3 = (min if min > 0 else 0) * 5 / 100
    min = 600000 - 400000 if money > 600000 else money - 400000
    sum4 = (min if min > 0 else 0) * 3 / 100
    min = 1000000 - 600000 if money > 1000000 else money - 600000
    sum5 = (min if min > 0 else 0) * 1.5 / 100
    min = money - 1000000 if money > 1000000 else 0
    sum6 = (min if min > 0 else 0) * 1 / 100

    return sum1 + sum2 + sum3 + sum4 + sum5 + sum6


# 解法二:
def get_money2(money):
    sum = 0
    if money < 100000:
        sum = money * 10 / 100
    elif money < 200000:
        sum = 100000 * 10 / 100 + (money - 100000) * 7.5 / 100
    elif money < 400000:
        sum = 100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100 + (money - 200000) * 5 / 100
    elif money < 600000:
        sum = (100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100 + (400000 - 200000) * 5 / 100
               + (money - 400000) * 3 / 100)
    elif money < 1000000:
        sum = (100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100 + (400000 - 200000) * 5 / 100
               + (600000 - 400000) * 3 / 100 + (money - 600000) * 1.5 / 100)
    else:
        sum = (100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100 + (400000 - 200000) * 5 / 100
               + (600000 - 400000) * 3 / 100 + (1000000 - 600000) * 1.5 / 100 + (money - 1000000) * 1 / 100)
    return sum


# 解法三:
def get_money3(money):
    arrmoney = [1000000, 600000, 400000, 200000, 100000, 0]
    arrrate = [0.01, 0.015, 0.03, 0.05, 0.07, 0.1]
    sum = 0
    for i in range(len(arrmoney)):
        if money > arrmoney[i]:
            sum += (money - arrmoney[i]) * arrrate[i]
            money = arrmoney[i]
    return sum


print(get_money(10000000))
print(get_money2(10000000))
print(get_money3(10000000))
