# coding: cp1252

from unicodedata import normalize, name

def unicode2ascii(u):
    return normalize('NFKD', u).encode('ASCII','ignore')

for i in range(128,256):
    c = chr(i)
    try:
        u = c.decode('cp1252')
    except UnicodeDecodeError:
        u = '?'
        descr = 'UnicodeDecodeError'
    else:
        descr = name(u)
    a = unicode2ascii(c) 
    print '%3d\t%r\t%s\t%s' % (i, c, a, descr)
