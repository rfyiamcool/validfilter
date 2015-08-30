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
