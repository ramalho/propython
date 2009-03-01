#!/usr/bin/env python
# coding: utf-8

import socket
 
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345
 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
 
for i in range(3):
    print 'Enviando pacote %d...' % i
    message = 'Este texto é a carga do pacote %d.' % i
    client.sendto(message, (SERVER_ADDRESS, SERVER_PORT))
 
client.close()

