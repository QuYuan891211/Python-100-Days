#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2020/4/14 20:05
# @Author  : yq
# @Site    : 
# @File    : my_conversion.py
# @Software: PyCharm
from builtins import float, input

value = float(input('请输入长度'))
unit = input('请输入单位')
if unit == 'in' or unit == '英寸':
    print ('%f英寸 = %f厘米' % (value, value*2.54))
elif unit == 'cm' or unit == '厘米':
    print ('%f厘米 = %f英寸' % (value, value/2.54))
else:
    print ('请输入有效单位')
