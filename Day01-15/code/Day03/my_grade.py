#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2020/4/14 20:19
# @Author  : yq
# @Site    : 
# @File    : my_grade.py
# @Software: PyCharm
from builtins import input, float

score = float(input('输入成绩'))
if score>89:
    print ('A')
elif score >79:
    print ('B')
elif score > 69:
    print ('c')
elif score > 59:
    print ('D')
else:
    print ('E')