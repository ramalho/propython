#!/usr/bin/env python
# coding: utf-8
import socket
 
PORT = 12345

# o tamanho maximo do datagrama é 64K, 
# com 65507 bytes utilizaveis sobre IPv4
# ver: http://en.wikipedia.org/wiki/User_Datagram_Protocol
BUFLEN = 1024 
 
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.bind(('', PORT))
 
while True:
    (message, address) = server.recvfrom(BUFLEN)
    print 'Pacote recebido de %s:%d' % (address[0], address[1])
    print 'Dados:\n"""%s"""' % message

