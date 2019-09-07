# js和jquery的区别

### 目录

[TOC]

### 获取元素：

js获取元素：

```js
document.getElementById("id");　             //根据id获取：　
document.getElementsByClassName("className");//根据类名获取：
document.getElementsByTagName("tagName");    //根据标签获取：
```

jquery获取元素：

```js
$("#id"); 　　//根据id获取
$(".class"); //根据类名获取
$("tag");    //根据标签获取
```

### 事件

js的各种事件比jquery都多了一个on

比如说js的鼠标点击事件：onclick=function(){};

而jquery只需要click(function(){})

**三、获取父节点、兄弟结点等**

js获取结点：（js不能直接获取除某一个结点之外的所有节点，比如说：tab栏切换，有另一种写法，见[js的tab栏切换案例](https://www.cnblogs.com/alex-xxc/p/10003523.html)）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
　　var test = document.getElementById("test");
　　var parent = test.parentNode; // 父节点
　　var chils = test.childNodes; // 全部子节点
　　var first = test.firstChild; // 第一个子节点
　　var last = test.lastChile; // 最后一个子节点　
　　var previous = test.previousSibling; // 上一个兄弟节点
　　var next = test.nextSbiling; // 下一个兄弟节点
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

jquery获取结点：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
    $("#test1").parent(); // 父节点
    $("#test1").parents(); // 全部父节点
    $("#test1").parents(".mui-content");
    $("#test").children(); // 全部子节点
    $("#test").children("#test1");
    $("#test").contents(); // 返回#test里面的所有内容，包括节点和文本
    $("#test").contents("#test1");
    $("#test1").prev();  // 上一个兄弟节点
    $("#test1").prevAll(); // 之前所有兄弟节点
    $("#test1").next(); // 下一个兄弟节点
    $("#test1").nextAll(); // 之后所有兄弟节点
    $("#test1").siblings(); // 所有兄弟节点
    $("#test1").siblings("#test2");
    $("#test").find("#test1");
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 **三、下拉框事件**

```
js下拉框事件：
$("course").addEventListener("change", function () {})
jquery下拉框事件：
$("course").change(function(){})
```

 

**四、获取值或内容**

 

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
js获取值或内容：
    如获取input的值：document.getElementById("ID").value
    如获取div的内容：document.getElementById("ID").innerText
                   document.getElementById("ID").innerHtml
jquery获取值或内容：
　　如获取input的值：$("id").val()    如获取div的内容：$("id").text(); $("id").html(); 
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 **四、获取offset值**

```
js:document.getElementById("id").offsetLeft
jquery:$("#id").offset().left
```