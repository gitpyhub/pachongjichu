#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

# 代理开关，表示是否启用代理
proxyswitch = False

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
httpproxy_handler = urllib2.ProxyHandler({"http" : "124.88.67.54:80"})

# 构建了一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)

#如果是gbk的就编码一下
#print response.read().decode("gbk")
#如果是utf-8的就直接输出
print response.read()
