[TOC]
### 如何学习CSS
    理解 CSS 的基本语法。
    理解盒子模型。
    理解文档流和定位。
    理解浮动和清除。
    理解各种 CSS 样式。
    目前发现的最好的资源是：http://www.w3school.com.cn/css/index.asp，将这里的教程看一边就够了。
    框架地址：http://happy.codeplex.com 
    博客地址：http://www.cnblogs.com/happyframework


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

文本框 text
placeholder 提示信息

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
    transparent 设置颜色透明
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
```css
/* 浮动功能: */
float:left/right;
/* 清除浮动 */
overflow:hidden;
clear:left/right/both
```

## 定位:
```css
/* 定位: 相对定位/绝对定位/固定定位  */
postion:relative/absolute/fixed
left:10px;
top:10px;
right:10px;
bottom:10px;
```
## 背景相关
```css
/* 背景色 */
background-color:red;
/* 背景图片 */
background-image:"../img/1.jpg"
/* 是否重复平铺 */
background-repeat: repeat/repeat-x/repeat-y/no-repeat
/* 背景图片的坐标,默认为左上角 */
background-position:x y; /* x y可以设置像素,也可以设置 left center right/top center botttom */
/* 背景图片的像素 */
background-size:width height /*width height 可以设置像素和百分比*/
```    

## 文本相关
```css
/* 文本大小,粗细,斜体,字体名称 */
font-size:10px;
font-weight:normal/bold;
font-style:italic; 
font-family:Arial,"黑体","Microsoft YaHei";/* 浏览器支持的字体不一样,所以可以有多个字体备选*/
/* 简写 zise 和 family 必须要写 */
font:style weight size family;

/* 文本颜色,装饰线,对齐方式,行高 */
color:red;
text-decoration:underline/overline/line-through/none;/* 下划线...*/
text-align:left/center/right;
/* 文本行高: height值为像素,可以通过 height 来设置文字在父元素中的垂直位置,height等于父元素的高度就是垂直居中*/
line-height:height;

/* 鼠标移上去的效果 伪类的 hover */
:hover
```

## 超链接相关
```css
/* 去除超链接的下划线 */
```

## 无序列表
```css
/* 清除列表前面的原点 */
list-style-type:none;
```

## 拖动条
```html
<input type="range" min="1" max="10" value="1">
```
<html>
<body>
<input type="range" min="1" max="10" value="1">
</body>
</html>

## 分组元素
```html
<!-- 分组元素 -->
<fieldset>
    <!-- 分组元素标题 -->
    <legend>改变背景颜色</legend>
    <div class="btns">
        <button>蓝色</button>
        <button>红色</button>
        <button>黄色</button>
    </div>
</div>
</fieldset>
```
<html>
<body>
<!-- 分组元素 -->
<fieldset>
    <!-- 分组元素标题 -->
    <legend>改变背景颜色</legend>
    <div class="btns">
        <button>蓝色</button>
        <button>红色</button>
        <button>黄色</button>
    </div>
</div>
</fieldset>
</body>
</html>