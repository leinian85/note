
# 1 2 3 6 9 18 27 54 57 111
# 1 2 3 6 12 13 25 50
# 6 12 15 27 54 57 111



if_exists_3 = False

def get_num2(num):
    global if_exists_3
    if num <= 3:
        if if_exists_3 and num == 2:
            list.pop(0)
            num = 4

        for i in range(num-1,0,-1):
            if i not in list:
                list.insert(0, i)
        return

    if num % 2 == 0:
        last_num = int(num / 2)
        list.insert(0, last_num)
        get_num2(last_num)
    else:
        last_num = int(num/2)+1
        if last_num % 2 == 0:
            last_num += 1
        last_num2 = num-last_num
        if last_num - last_num2 == 3:
            if_exists_3 = True
        list.insert(0, last_num)
        list.insert(0, last_num2)
        get_num2(last_num2)

def check():
    max_num = list[-1]
    for i in range(len(list)):
        last_num1 = list.pop()
        last_num2 = list[-1]
        num = last_num1-last_num2
        if num not in list:
            print('错误:',max_num)
            return
        list.pop()
        if len(list)<3:
            return


for i in range(3,1000):
    list = [i]
    get_num2(i)
    print(str(i)+"共{}步:".format(len(list)),list)
    check()

# i = 7
# list = [i]
# get_num2(i)
# print(list)

