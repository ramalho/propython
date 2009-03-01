#!/usr/bin/env python

from getch import getch
from sys import stdout

CR = chr(13)

print "Tecle [x] para sair"
while True:
    c = getch()
    if c == CR:
        print
    elif c == 'x':
        break
    else:
        stdout.write(c)
print
    