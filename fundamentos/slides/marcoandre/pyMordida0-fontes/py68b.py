#!/usr/bin/env python
#-*- coding:utf-8 -*-

class C(object):
    def __init__(self, x=0):
#        self.__x = x
        self.setx(x)
    def getx(self):
        return self.__x
    def setx(self, x):
        if x < 0: x = 0
        self.__x = x
    x = property(getx, setx)
