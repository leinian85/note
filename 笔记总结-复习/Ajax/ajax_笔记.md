ajax

作用:

异步请求

适用场合:

1.搜索建议

2.表单验证

3.前后端分离



xhr

```js
# IE7+使用
xhr = new XMLHttpRequest()
xhr.open(method['get'/'post'],url,asyn[true/false])
# 监听xhr的readystate的状态变化
xhr.onreadystatechange
# 相应数据
xhr.responseText
xhr.setRequestHeader('ContentType','application/x-www-form-urlencoded')
# 请求数据:name=wangdachui&age=21
xhr.send([请求数据])
```



JSON

1.用{}表示单个对象

2.键值对

3.键要用""



#前端

$arr.each(function(index,obj){})

$.each(arr,function(index,obj){})



#后端

#返回 json 字符串

import json

jsonstr = json.dumps([列表/字典/元组])







#前端

JSON对象 = json.parse(JSON字符串)



1.$obj.load(url,data,callback)

请求:

get请求的请求头没有 Content-Type

post请求有 Content-Type

相应:

响应头中一定有 Content-Type



$.get(url,data,callback,type)

默认不传参时发GET请求