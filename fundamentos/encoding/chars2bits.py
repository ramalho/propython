#!/usr/bin/env python
# coding: utf-8

from unicodedata import name

def bits(n):
    return ''.join(reversed([str((n>>i)&1) for i in range(64)])).lstrip('0')

CHARS = u'''A a Ã ã € 語'''.split()

for c in CHARS:
    utf = c.encode('utf-8')
    bytes = ' '.join([bits(ord(b)) for b in utf]) 
    print '%5d %04x %s %32s | %s' % (ord(c), ord(c), c, bits(ord(c)), bytes)
    print name(c)
    
print '-' * 60    
for i in range(128,256):
    try:
        c = chr(i).decode('cp1252')
    except UnicodeDecodeError:
        print '%3d   -' % i
    else:  
        utf = c.encode('utf-8')
        bytes = ' '.join([bits(ord(b)) for b in utf])
        cod = str(ord(c)) if ord(c) != i else '....' 
        print '%3d %4s %04x %s %16s | %s' % (i , cod, ord(c), c, bits(ord(c)), bytes)
