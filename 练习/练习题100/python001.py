# 题目001：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 解法一:
# list01 = [1,2,3,4]
# num = 0
# for a in list01:
#     for b in list01:
#         if b!= a:
#             for c in list01:
#                 if a!= c and b!= c:
#                    num+=1
#                    print(str(a)+str(b)+str(c))
# print("总数:%d"%num)

# 解法一:用递归来解
list01 = []
def get_num(lens,num,list_num):
    if len(num) == lens:
        list01.append(num)
        return

    for i in range(len(list_num)):
        if str(list_num[i]) not in list(num):
            n = str(num)+str(list_num[i])
            get_num(lens,n,list_num)

list_num=[1,2,3,4]
get_num(1,"",list_num)
print(list01)
print("总数:%d"%len(list01))