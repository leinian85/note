[TOC]

# 数据分析必备的43个Excel函数

**Excel**是我们工作中经常使用的一种工具，对于数据分析来说，这也是处理数据最基础的工具。很多传统行业的数据分析师甚至只要掌握Excel和SQL即可。

对于初学者而言，有时候并不需要急于苦学R语言等专业工具（当然，学会了就是加分项），因为**Excel涵盖的功能足够多，也有很多统计、分析、可视化的插件**等，只不过我们平时处理数据的时候对于许多函数都不知道怎么用！

对于Excel的进阶学习，主要分为两块——一个是数据分析常用的Excel函数，另一个是用Excel做一个简单完整的分析。



这篇文章主要介绍数据分析**常用的43个Excel函数及用途**，实战分析将在下一篇讲解。

#### **关于函数：**

## 函数分类介绍：

下面根据不同的运用场景，对这些常用的必备函数进行分类介绍。

### 一、关联匹配类

经常性的，需要的数据不在同一个Excel表或同一个Excel表不同sheet中，数据太多，copy起来麻烦还容易出错，如何整合呢？

下面这些函数就是用于**多表关联**或者**行列比对**时的场景，而且表格越复杂，用起来越爽！

**1、VLOOKUP**

功能：用于查找**首列满足条件的元素**。

语法：=VLOOKUP（要查找的值，要在其中查找值的区域，区域中包含返回值的列号，精确匹配或近似匹配 – 指定为 0/FALSE 或 1/TRUE）。

（举例：查询姓名是F5单元格中的员工是什么职务）



![img](https://upload-images.jianshu.io/upload_images/15400793-6ac803de8524b7da.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/498/format/webp)

**2、HLOOKUP**

功能：搜索表的顶行或值的数组中的值，并在表格或数组中指定的行的同一列中返回一个值。

语法：=VLOOKUP（要查找的值，要在其中查找值的区域，区域中包含返回值的行号，精确匹配或近似匹配 – 指定为 0/FALSE 或 1/TRUE）。

区别：函数HLOOKUP和VLOOKUP都是用来在表格中查找数据，但是，HLOOKUP返回的值与需要查找的值在同一列上，而VLOOKUP返回的值与需要查找的值在同一行上。

**3、INDEX**

功能：返回表格或区域中的值或引用该值。

语法：= INDEX(要返回值的单元格区域或数组,所在行,所在列)



![img](https://upload-images.jianshu.io/upload_images/15400793-fa2a30c397cee081.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/385/format/webp)

**4、MATCH**

功能：用于返回指定内容在指定区域（某行或者某列）的位置。   

语法：= MATCH (要返回值的单元格区域或数组，查找的区域，查找方式)

**5、RANK**

功能：求某一个数值在某一区域内一组数值中的排名。

语法：=RANK(参与排名的数值, 排名的数值区域, 排名方式-0是降序-1是升序-默认为0）。

**6、Row**

功能：返回单元格所在的行

**7、Column**

功能：返回单元格所在的列

**8、Offset**

功能：从指定的基准位置按行列偏移量返回指定的引用

语法：＝Offset（指定点，偏移多少行，偏移多少列，返回多少行，返回多少列）

#### **二、清洗处理类**

数据处理之前，需要对提取的数据进行初步清洗，如清除字符串空格，合并单元格、替换、截取字符串、查找字符串出现的位置等。

*清除字符串空格：使用Trim/Ltrim/Rtrim*

*合并单元格：使用concatenate*

*截取字符串：使用Left/Right/Mid*

*替换单元格中内容：Replace/Substitute*

*查找文本在单元格中的位置：Find/Search*

**9、Trim**

功能：清除掉字符串两边的空格

**10、Ltrim**

功能：清除单元格右边的空格

**11、Rtrim**

功能：清除单元格左边的空格

**12、concatenate**

语法：=Concatenate(单元格1，单元格2……)

合并单元格中的内容，还有另一种合并方式是&，需要合并的内容过多时，concatenate效率更快。

**13、Left**

功能：从左截取字符串

语法：=Left(值所在单元格，截取长度)

**14、Right**

功能：从右截取字符串

语法：= Right (值所在单元格，截取长度)

**15、Mid**

功能：从中间截取字符串

语法：= Mid（指定字符串，开始位置，截取长度）

（举例：根据身份证号码提取年月）



![img](https://upload-images.jianshu.io/upload_images/15400793-e31f7d9cc5f078eb.png?imageMogr2/auto-orient/strip|imageView2/2/w/509/format/webp)

**16、Replace**

功能：替换掉单元格的字符串

语法：=Replace（指定字符串，哪个位置开始替换，替换几个字符，替换成什么）

**17、Substitute**

和replace接近，不同在于Replace根据位置实现替换，需要提供从第几位开始替换，替换几位，替换后的新的文本；而Substitute根据文本内容替换，需要提供替换的旧文本和新文本，以及替换第几个旧文本等。因此Replace实现固定位置的文本替换，Substitute实现固定文本替换。

（举例：替换部分电话号码）



![img](https://upload-images.jianshu.io/upload_images/15400793-5991a6e51781679a.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/557/format/webp)

**18、Find**

功能：查找文本位置

语法：=Find（要查找字符，指定字符串，第几个字符）

**19、Search**

功能：返回一个指定字符或文本字符串在字符串中第一次出现的位置,从左到右查找

语法：=search（要查找的字符，字符所在的文本，从第几个字符开始查找）

区别：Find和Search这两个函数功能几乎相同，实现查找字符所在的位置，区别在于Find函数精确查找，区分大小写；Search函数模糊查找，不区分大小写。

**20、Len**

功能：文本字符串的字符个数

**21、Lenb**

功能：返回文本中所包含的字符数

（举例：从A列姓名电话中提取出姓名）



![img](https://upload-images.jianshu.io/upload_images/15400793-6fd6f86b11fb96b7.png?imageMogr2/auto-orient/strip|imageView2/2/w/358/format/webp)

#### **三、逻辑运算类**

逻辑，顾名思义，不赘述，直接上函数：

**22、IF**

功能：使用逻辑函数IF 函数时，如果条件为真，该函数将返回一个值；如果条件为假，函数将返回另一个值。

语法：=IF(条件, true时返回值, false返回值)



![img](https://upload-images.jianshu.io/upload_images/15400793-d8ddf4084cf65cb2.png?imageMogr2/auto-orient/strip|imageView2/2/w/346/format/webp)

**23、AND**

功能：逻辑判断，相当于“并”。

语法：全部参数为True，则返回True，经常用于多条件判断。

**24、OR**

功能：逻辑判断，相当于“或”。

语法：只要参数有一个True，则返回Ture，经常用于多条件判断。

#### **四、计算统计类**

在利用Excel表格统计数据时，常常需要使用**各种Excel自带的公式**，也是最常使用的一类。（对于这些，Excel自带快捷功能）

*MIN函数：找到某区域中的最小值*

*MAX函数：找到某区域中的最大值*

*AVERAGE函数：计算某区域中的平均值*

*COUNT函数： 计算某区域中包含数字的单元格的数目*

*COUNTIF函数：计算某个区域中满足给定条件的单元格数目*

*COUNTIFS函数：统计一组给定条件所指定的单元格数*

*SUM函数：计算单元格区域中所有数值的和*

*SUMIF函数：对满足条件的单元格求和*

*SUMIFS函数：对一组满足条件指定的单元格求和*

*SUMPRODUCT函数：返回相应的数组或区域乘积的和*

**25、MIN**

功能：找到某区域中的最小值

**26、MAX函数**

功能：找到某区域中的最大值

**27、AVERAGE**

功能：计算某区域中的平均值

**28、COUNT**

功能：计算含有数字的单元格的个数。

**29、COUNTIF**

功能：计算某个区域中满足给定条件的单元格数目

语法：=COUNTIF(单元格1: 单元格2 ,条件)

比如=COUNTIF(Table1!A1:Table1!C100, “YES” ) 计算Table1中A1到C100区域单元格中值为”YES”的单元格个数

（举例：统计制定店铺的业务笔数）



![img](https://upload-images.jianshu.io/upload_images/15400793-d333c194d78167cb.png?imageMogr2/auto-orient/strip|imageView2/2/w/427/format/webp)

**30、COUNTIFS**

功能：统计一组给定条件所指定的单元格数

语法：=COUNTIFS(第一个条件区域，第一个对应的条件，第二个条件区域，第二个对应的条件，第N个条件区域，第N个对应的条件)

比如：=COUNTIFS(Table1!A1: Table1!A100, “YES”,Table1!C1: Table1!C100, “NO” ) 计算Table1中A1到A100区域单元格中值为”YES”,而且同时C区域值为”NO”的单元格个数

**31、SUM**

计算单元格区域中所有数值的和

**32、SUMIF**

功能：求满足条件的单元格和

语法：=SUMIF(单元格1: 单元格2 ,条件,单元格3: 单元格4)

（举例：计算一班的总成绩）



![img](https://upload-images.jianshu.io/upload_images/15400793-2edf7493b6604b91.png?imageMogr2/auto-orient/strip|imageView2/2/w/538/format/webp)

**32、SUMIFS**

功能：对一组满足条件指定的单元格求和

语法：=SUMIFS（实际求和区域，第一个条件区域，第一个对应的求和条件，第二个条件区域，第二个对应的求和条件，第N个条件区域，第N个对应的求和条件）。比如=SUMIFS(Table1!C1:Table1!C100，Table1!A1: Table1!A100, “YES” ,Table1!B1:Table1B100, “NO” ) 计算Table1中C1到C100区域,同时相应行A列值为”YES”，而且对应B列值为”NO”的单元格的和。

**33、SUMPRODUCT**

功能：返回相应的数组或区域乘积的和

语法：=SUMPRODUCT(单元格1: 单元格2 ,单元格3: 单元格4)

比如：=SUMPRODUCT(Table1!A1:Table1!A100, Table2!B1Table2!B100) 计算表格1的A1到A100与表格2的B1到B100的乘积和，即A1*B1+A2*B2+A3*B3+…

**34、Stdev**

统计型函数，求标准差。

**35、Substotal**

语法：=Substotal（引用区域，参数）

汇总型函数，将平均值、计数、最大最小、相乘、标准差、求和、方差等参数化，换言之，只要会了这个函数，上面的都可以抛弃掉了。

**36、Int／Round**

取整函数，int向下取整，round按小数位取数。

round(3.1415,2)=3.14 ;

round(3.1415,1)=3.1

#### **五、时间序列类**

专门用于处理时间格式以及转换。

**37、TODAY**

返回今天的日期，动态函数。

**38、NOW**

返回当前的时间，动态函数。

**39、YEAR**

功能：返回日期的年份。

**40、MONTH**

功能：返回日期的月份。

**41、DAY**

功能：返回以序列数表示的某日期的天数。

**42、WEEKDAY**

功能：返回对应于某个日期的一周中的第几天。 默认情况下，天数是1（星期日）到 7（星期六）范围内的整数。

语法：=Weekday(指定时间，参数)

**43、Datedif**

功能：计算两个日期之间相隔的天数、月数或年数。

语法：=Datedif（开始日期，结束日期，参数）





以上，就是本人整理出来常用并且学会之后无比爽的Excel函数，希望能够帮到大家！

欢迎留言交流！

[十周入门数据分析]正在公号更新，也欢迎来交流！