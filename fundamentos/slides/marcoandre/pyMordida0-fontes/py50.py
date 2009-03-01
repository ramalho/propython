#!/usr/bin/env python
#-*- coding:utf-8 -*-

total=0
while True:
    p = raw_input('+')
    if not p.strip(): break
    try:
        total += float(p)
    except ValueError:
        print "."
print '---------'
print total
