#!/usr/bin/env python
#-*- coding:utf-8 -*-

class C(object):
    def __init__(self, x):
        self.__x = x
    @property
    def x(self):
        return self.__x

