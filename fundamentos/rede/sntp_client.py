#!/usr/bin/env python

'''
autor: Simon Foster
fonte: http://code.activestate.com/recipes/117211/
adaptado por: Luciano Ramalho

servidor SNTP no Brasil:
200.144.121.33: ntp.cais.rnp.br 
'''

import socket
import sys
from struct import unpack
from time import localtime, strftime

TIME1970 = 2208988800L      # Thanks to F.Lundh

soq = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
req = '\x1b' + 47 * '\0'
soq.sendto( req, (sys.argv[1], 123 ))
resp, ender = soq.recvfrom( 1024 )
if resp:
    t = localtime(unpack( '!12I', resp )[10] - TIME1970)
    ts = strftime('%H:%M:%S', t)
    print 'Resposta de %s: %s' % (ender, ts)

