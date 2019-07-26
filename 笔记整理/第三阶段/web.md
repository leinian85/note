[TOC]
### table 表格
    创建一个3行4列的表格
    table>tr*3>td*3

### form 表单


### CSS
```html
<标签名 style="样式声明">
.e.g:
<div style="属性:值;属性:值">
```

    创建样式文件,扩展名用 .css
    样式表中,#后面跟id,*表示所有,.后面跟类别,没有#和.表示标签
    id选择器/标签选择器/class选择器
```css
#p1{
    color:red;
}
*{
    margin: 0px;
    padding: 0px;
}
p{
    color: cyan
}
.blue{
    color: blue
}
```
    在使用的页面的<head></head>中用link引入
```html
<link rel="stylesheet" href="../css/index.css">
```
### 伪类

### 元素的尺寸和颜色
    1.元素的尺寸
    (1).px像素单文
    (2).百分比 % 相对父元素
    (3).相对单位 em 相对父元素 1em = 16px (用于移动端,常用 1.5em)
    (4).rpx (微信小程序页面的单位)
    (5).当页面的元素的大小超出元素的宽度,可以使用 overflow 属性设置超出部分的显示方式,建议使用 overflow:auto

    2.颜色
    (1).元素的字体,背景,边框 都有颜色
    (2).使用方式 
    (2-1)英文单词
    (2-2)16进制:长的16进制/短的16进制
    (2-3)rgb:rgb(2,3,5)
    (2-4)rgba(0~1):rgba(2,3,5,0.5)  0.5表示透明度

```css
color:red
color:#ffffff;#000000
color:#fff,#000
color:rgb(2,3,5)
color:rgba(2,3,5)
```

### 盒子模型


**固定宽度的元素的居中实现方式:**

```css
margin:0 auto
```

#### 边框
```css
boder:width style color;
```
    style:
        solid	实线边框
        dotted	点线边框
        dashed	虚线边框
        double	双线边框

单边框设置:分别设置某一方向的边框，取值：width style color;
```css
border-top	设置上边框
border-bottom	设置下边框
border-left	设置左边框
border-right	设置右边框
```

    实体边框由4个三角形组成
    transparent 设置透明颜色透明
```css
border-bottom-color: transparent;
```

圆角边框:
```css
border-radius: 300px 150px 150px 300px;
```
### 盒子模型
1.盒模型属性:

    boder 边框
    border-radius 圆角边框
    outline 轮廓线
    box-shadow 阴影
    padding 内边距
    margin 外边距
    overflow 填充
```css
overflow: hidden;#自动填充/自动适配
```
>外边距合并:
上下相遇合并
!["合并"](./img/margin-unite1.png "")
<a href="./source_code/03-margin.html">示例</a>
内外包裹合并
!["合并"](./img/margin-unite2.png "")
<a href="./source_code/04-margin.html">示例</a>
2.属性值:
    
    transparent 设置颜色透明

## 浮动布局
1.属性:
```
    float:left/right
```

2.清除浮动
```
    clear:left/right/both
```