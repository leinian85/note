# 题目004：输入某年某月某日，判断这一天是这一年的第几天？
import time

def get_days(year,month,day):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    for i in range(len(month_list)):
        if i+1 < month:
            sum += month_list[i]
    return sum + day

def get_day2(datestr):
    td = time.strptime(datestr,'%Y-%m-%d')
    return td.tm_yday

print(get_days(2019,10,10))
print(get_day2('2019-10-10'))