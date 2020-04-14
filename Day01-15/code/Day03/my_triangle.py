#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2020/4/14 20:31
# @Author  : yq
# @Site    : 
# @File    : my_triangle.py
# @Software: PyCharm
from builtins import float, input

a = float(input('a'))
b = float(input('b'))
c = float(input('c'))
if a + b > c or b + c > a or c + a > b:
    p = a + b + c
    print('周长为%f' % p)
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print('面积为%f' % s)
