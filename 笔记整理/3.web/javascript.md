[TOC]
# JavaScript

## 使用javascript的三种方式
    1. 属性绑定
```html
<input onclick="alert('你点了我')" type="button" value="点一下">
```
    2. script标签内嵌使用
```html
<!-- 可以放在html文件的任意位置 head/body -->
<script>
    alert("我在head里面");
</script>
```
    3. script标签外部引入
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

## 操作body的方法
```JavaScript
document.body.style.backgroundColor = color;
```

## 语法
### 变量定义
```JavaScript
a = 2;
var b = c = 1;
var d = 3,e = 4;
```
### 数据类型
    1.字符 string
    2.数字 number
    3.布尔 boolean
    4.不确定形
    5.null

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
### 异常处理
```JavaScript
try {
    console.log(a)
} catch (error) {
    console.log(error.message)
}
```

### 分支语句 if...else
```JavaScript
if(条件){

}else if(条件){

}else{

}

// 以下都为 false
if(0){}
if(0.0){}
if(""){}
if(undefined){}
if(NaN){}
if(null){}
```

### 分支语句 switch
```JavaScript 
// break不能少,否则会走到下一个分支
switch(){}
case 值1:
    break;
case 值2:
    break;
default:
    break;
}
```

### 循环语句 for/while/do while
```JavaScript
for(i=0;i<=10;i++){
    循环体;
}

while(条件){
    循环体;
}

do{
    循环体;
}while(条件)

// 跳出循环
break
continue
```

## 自定义并使用函数
```Javascript
<javascript>
    function fun01(){

    }
</javascript>
```
```html
<button onclick="fun01()" >按钮</button>
```

## 

## 鼠标
```JavaScript
cursor: pointer; // 手的形状
cursor: move; // 可以移动的形状
```

## 函数
```JavaScript
// 正常定义函数
function a(name,age){
    return name + "的年龄是:" + age;
}

// 定义匿名函数
(function(name,age){
    var str = name + "的年龄是:" + age;
    div.innerText = str
})("张三",19)

// json 格式定义函数,不能在匿名函数中使用
var log{
    a:function(){
        return "OK";
    },
    b:function(){
        return "NO";
    }
}
tip = document.getElementById("tip");
tip.innerText = log.a(); 

```

### 错误信息
Cannot set property 'onclick' of null
出现这个错误的原因是页面加载的先后顺序导致的,先加载JS,由于还没有控件,使用报错

### 定时器
#### 间歇调用的定时器 setInterval
```JavaScript
function show(){
    console.log("OK");
};
// setInterval调用的时候函数只写名字,不能加括号
// 定时器的间隔时间的单位默认是毫秒
var taskId = setInterval(show, 1000);

function close(){
    clearInterval(taskId); // 停止计时器对象
};
// 绑定按钮功能的时候也只写函数名,不加括号
$$("btn").onclick = close;
```

#### 超时/延时定时器(一次性调用) setTimeOut
    作用:等待多久之后执行一次代码

### 超链接
```JavaScript
// 设置超链接不跳转
<a href="Javascript:;">不跳转</a>
```

### 获取焦点
```JavaScript
// 样式:鼠标指上去的效果
span:hover{
    color: black;
    text-decoration:none; // 下划线设置为空
}
// 事件:鼠标指上去的效果
onmouseover
```
