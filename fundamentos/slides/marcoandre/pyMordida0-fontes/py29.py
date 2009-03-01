#!/usr/bin/env python
#-*- coding:utf-8 -*-

l = [1,-2,3,-1,-3,4]
l2 = [n*10 for n in l]
l3 = [n for n in l if n > 0]
l4 = [n*10 for n in l if n > 0]

print l
print l2
print l3
print l4

