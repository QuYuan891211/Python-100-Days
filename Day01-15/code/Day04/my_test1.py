#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2020/4/14 21:09
# @Author  : yq
# @Site    : 输入一个数判断是否为素数
# @File    : my_test1.py
# @Software: PyCharm
num = int(input('输入数字'))
is_prime = True
for x in range(2, num):
    if num % x == 0:
        print('%d 不是一个素数' % num)
        is_prime = False
        break
if is_prime:
    print('%d 是一个素数' % num)
