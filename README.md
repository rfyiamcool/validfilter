#`validict`

## 简单描述

`validict` is a Python module for comparing an unknown value to a desired template. It is intended for the top-level type to be a `dict`, but should be flexible enough to deal with `list`s or scalars (though if you're dealing at scalars, might I suggest running away from this and just using Python's `isinstance`). *Important: this library specifically does not treat `tuple`s as template expectations but instead as a set of expectations for a given position in a template.*

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
