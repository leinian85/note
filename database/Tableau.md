# 除了Excel你可能还需要Tableau

2018.01.15 17:38:18字数 854阅读 5570

Excel相信是很多人用得最多的数据处理工具，但是Excel在数据可视化方面功能还有所欠缺。[Tableau](https://link.jianshu.com/?t=http%3A%2F%2Fwww.tableau.com)可能刚好是你需要的，它是一个专们用于数据可视化的工具。主要有以下几个功能：

1、支持多种数据源
2、支持数据源连接查询
3、支持计算字段
4、丰富的图表可视化配置
5、支持数据钻取
6、支持地理信息数据
7、支持仪表盘

下面针对提到的特性说明一下：

# 强大的数据源支持

支持的数据源主要有两大类，一类是文件，一类是服务器。基本上常见的数十种数据源都支持。数据源还支持实时或者是提取到本地（以增强性能），同时还提供数据源级别的筛选器可以过滤部分数据。

![img](https://upload-images.jianshu.io/upload_images/3098420-d840a3b8e72904eb.png?imageMogr2/auto-orient/strip|imageView2/2/w/555)

Tableau 支持的数据源

# 数据集连接查询

这个功能类似于SQL里面的Left join、Inner Join等。可以连接多个数据集生成一个新的数据集

![img](https://upload-images.jianshu.io/upload_images/3098420-2a3b99a624b7ff52.png?imageMogr2/auto-orient/strip|imageView2/2/w/526)

数据集连接

# 计算字段

如果只能显示静态数据的话显然不能满足我们的需求，因此Tableau还提供了强大的数据处理功能。Tableau在加载数据源之后会把字段信息以维度的形式呈现。

![img](https://upload-images.jianshu.io/upload_images/3098420-b4fe59defde67b8c.png?imageMogr2/auto-orient/strip|imageView2/2/w/204)

数据源维度

涉及到需要自定义计算类的内容，可以在度量窗口中“新建计算字段”根据表达式去创建计算字段。计算字段编辑器支持函数及逻辑、判断表达式等。

![img](https://upload-images.jianshu.io/upload_images/3098420-6e23196661df3437.png?imageMogr2/auto-orient/strip|imageView2/2/w/938)

计算字段编辑器

# 丰富的可视化配置

Tableau内置多种图表，可以在不改变数据集的情况下切换不同类别的的图表。

![img](https://upload-images.jianshu.io/upload_images/3098420-e7d76732186a5a1b.png?imageMogr2/auto-orient/strip|imageView2/2/w/202)

内置图表集

针对图表具体的颜色、大小、文本、工具提示也可以进行自定义配置。

![img](https://upload-images.jianshu.io/upload_images/3098420-9e62aca5a3af1c60.png?imageMogr2/auto-orient/strip|imageView2/2/w/157)

自定义图表标记

# 数据钻取

数据钻取是报表常用的功能，Tableau使把这个功能做得很人性化，基本上通过配置即可支持数据的钻取功能。比如自动识别日期字段，可以进行年、月、日等钻取。维度字段可以支持分层结构等。

![img](https://upload-images.jianshu.io/upload_images/3098420-c4f573026d62b801.png?imageMogr2/auto-orient/strip|imageView2/2/w/185)

自定义分层结构

![img](https://upload-images.jianshu.io/upload_images/3098420-e0fd2f13030dd91d.png?imageMogr2/auto-orient/strip|imageView2/2/w/511)

数据钻取

# 空间信息

如果我们要在Excel实现地图信息的话会比较麻烦，Tableau自带中国及世界地图。可以快速的根据原始数据画出带地图信息的图表。（数据源中省市名称不能带省或市，如北京市需改为 北京）。

![img](https://upload-images.jianshu.io/upload_images/3098420-e87637c5b49c5641.png?imageMogr2/auto-orient/strip|imageView2/2/w/649)

带地图信息的报表

# 仪表盘

仪表盘可以认为是多个报表的集合，方便查看同类的数据。使用Tableau可以灵活的创建基于报表的仪表盘。而且同一个仪表盘的不同报表之间数据是钻取是可以关联的。比如点击仪表盘中A报表的某个品类，同一个仪表盘的其他报表也会突出进行显示A品类相关连的数据。

![img](https://upload-images.jianshu.io/upload_images/3098420-4e8b4c07c5c82008.png?imageMogr2/auto-orient/strip|imageView2/2/w/273)

Tableau仪表盘

# 总结

Excel固然非常好，但如果你遇到需要频繁的处理同类数据、需要对数据进行多种维度的分析与处理时建议可以试试Tableau，可以节省你很多时间。