### 装饰器
```python
<<<<<<< HEAD
装饰器可以依照下面格式:
=======
# 装饰器可以依照下面格式:
>>>>>>> a90d5874db9b330c6e52e174d5e1fd51afb461f0
def verify_account(func):
    def wrapper(*args, **kwargs):
        ......
        return func(*args, **kwargs)
    return wrapper
<<<<<<< HEAD
```

=======

# 带参数的装饰器
# 装饰器允许传入参数，一个携带了参数的装饰器将有三层函数，如下所示：
def check(*method)
    def verify_account(func):
        def wrapper(*args, **kwargs):
            ......
            return func(*args, **kwargs)
        return wrapper
    return verify_account

# 多个装饰器,广度优先的原则
# eg.
def a(func):
    print('i\'m a!')
    def e():
        print(1)
        func()
        print(2)
    return e

def b(func):
    print('i\'m b!')
    def d():
        print('a')
        func()
        print('b')
    return d

@a
@b
def c():
    print('!!!!!')

c()
#输出结果:
i'm b!
i'm a!
1
a
!!!!!
b
2
```

>>>>>>> a90d5874db9b330c6e52e174d5e1fd51afb461f0
### 示例:
```python
# 需求：对以下两个功能增加权限验证.
"""
# 需要增加的功能
def verify_permissions():
    print("权限验证")

# 已有功能
def enter_background():
    verify_permissions()
    print("进入后台")

def delete_order():
    verify_permissions()
    print("删除订单")

enter_background()
delete_order()

# 缺点：增加新功能，需要修改已有功能．  [违反开闭原则]
"""

"""
# 需要增加的功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()

    return wrapper

# 已有功能
def enter_background():
    print("进入后台")

def delete_order():
    print("删除订单")

# enter_background = 新功能 + 旧功能
enter_background = verify_permissions(enter_background)
delete_order = verify_permissions(delete_order)

enter_background()
delete_order()
缺点：每次拦截对已有功能(enter_background)的调用,不科学.
"""

"""
# 需要增加的功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()

    return wrapper

# 已有功能
# enter_background = verify_permissions(enter_background)
@verify_permissions
def enter_background():
    print("进入后台")

@verify_permissions
def delete_order():
    print("删除订单")

enter_background()
delete_order()
缺点：如果已有功能参数不统一，则无法包装.
"""

def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("权限验证")
        func(*args, **kwargs)

    return wrapper


# 已有功能
@verify_permissions
def enter_background(login_id, pwd):
    print(login_id, pwd, "进入后台")

@verify_permissions
def delete_order(id):
    print("删除订单", id)

# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)

enter_background("abc", 1234)
delete_order(101)
```

