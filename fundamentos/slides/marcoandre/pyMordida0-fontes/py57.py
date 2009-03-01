#!/usr/bin/env python
#-*- coding:utf-8 -*-

a = [21, 52, 73]
b = a
c = a[:]

print "b é a?", b is a
print "c é a?", c is a
print "b é igual a a?", b == a
print "c é igual a a?", c == a

print a, b, c
b[1] = 99
print a, b, c

