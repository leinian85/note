[TOC]
## 数据类型:

>None

>int   例:1 ，2

>float 例:1.0 ，2.5

>str   例:"" ，"字符"

>bool  例:True ，False

>复数 　例:complex 

## 类型转换
>int(数据)
>float(数据)
>str(数据) 
>bool(数据) 

    如果数据的格式不正确，会错误。
        例如：int("100+")，int("1.23")
    如果数据表示"没有",转换结果为false
        bool(1) --> True
        bool("") -->False
        bool(0)  -->False

## 数据赋值内存图
!["None"](/day02/None.jpg)
!["变量交换"](/day02/变量交换.jpg)
!["变量内存图"](/day02/变量内存图.jpg)
