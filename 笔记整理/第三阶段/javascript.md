[TOC]
# JavaScript

## 使用javascript的三种方式
    1. 属性绑定
```html
<input onclick="alert('你点了我')" type="button" value="点一下">
```
    2. 内嵌使用
```html
<!-- 可以放在html文件的任意位置 head/body -->
<script>
    alert("我在head里面");
</script>
```
    3. 外部连接
```html
<!-- 需要创建外部的 js 文件 -->
<script src="../js/index.js"></script>
```

## 事件
    onclick 点击事件

## 函数
```JavaScript
1. 输入/输出语句:
  alert() 普通的网页弹出框
  promtp() 用于接收并返回用户输入的内容
  console.log() 控制台输出,用于调试
  document.write() 作用1:显示写入的内容 作用2:页面渲染完成之后再调用会重写页面的内容

2. 函数
  PI.toFixed(2); //保留2为小数
  a.charCodeAt(); //字符转换成数值
  Number(strNum); //转换成数字
  123.toString() //转换成字符串
  isNaN() //判断是否返回的 NaN
  document.getElementById("text") //通过ID获取对象
```
## 语法
### 变量定义
```JavaScript
a = 2;
var b = c = 1;
var d = 3,e = 4;
```

### 常量定义
```JavaScript
const PI = 3.1415926;
var pi = PI.toFixed(2); //保留2为小数

var streName = "张无忌";
var typeName = typeof (streName);

var isExit = false;
var typeBool = typeof (isExit);
```

### 转换
```JavaScript
var strNum = "3.14";
num = Number(strNum); // 转换成数字类型
intNum = parseInt(strNum); //转换成整形
floatNum = parseFloat(strNum); //转换成浮点型

strNUm2 = num.toString(); //转换成string
strToInt = parseInt(strNUm2); //转换成整形
strToFloat = parseFloat(strNUm2); //转换成浮点型
```