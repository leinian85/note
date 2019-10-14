[TOC]
### 1.字典推导式：
```
dict02 = {}
dict01 = {"a":10,"b":8,"c":5}
for k,v in dict01.items():
    dict02[k] = v**2
print(dict02)

dict03 = {k:v**2 for k,v in dict01.items()}
print(dict03)
```

### 2.列表推导式嵌套：
```
lista = ["a","b","c"]
listb = ["d","e"]
listc = []
for itema in lista:
    for itemb in listb:
	listc.append(itema+itemb) 
print(listd)

listd = [itema+itemb for itema in lista for itemb in listb]
print(listd)
```
