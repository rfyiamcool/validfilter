# validfilter

## 简单描述

一个用来验证数据格式的模块,已经加入了正则表达式的识别，后期会加入具体某个KEY的是否验证的标示

## 安装方法

shell~$ pip install validfilter

## 使用方法

```

#coding:utf-8
from validfilter import checkdata

template = {
    'name': 'xiaorui',
    'age': '.*',
    'url' : 'http://.*',
    'address': '\w*',
    'pets': [
        {
            'name': 'ying',
            'kind': '.*' 
        }
    ],
    'parents': [{'name': '.*'}], 
}

kid = {
    'name': "fengyun from xiaorui.cc",
    'age': 123,
    'url' : 'http://xiaorui.cc',
    'address': 'beijing',
    'pets': [
        {
        'name': "liliying", 
        'kind': "nima",
        },
    ],
    'parents': [
        {'name': "zhangbin"},
        {'name': "liudehua"}
    ]
}

print checkdata(template, kid) 
```

#### Run Result
```
python test.py
xiaorui fengyun from xiaorui.cc
http://.* http://xiaorui.cc
.* 123
.* zhangbin
.* liudehua
.* nima
ying liliying
\w* beijing
True
```


