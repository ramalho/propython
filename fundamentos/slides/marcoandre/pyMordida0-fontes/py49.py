#!/usr/bin/env python
#-*- coding:utf-8 -*-

total=0
while True:
    p = raw_input('+')
    if not p.strip(): break
    total += float(p)
print '---------'
print total
