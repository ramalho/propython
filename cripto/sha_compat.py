#!/usr/bin/env python
# coding: utf-8

from sys import version_info

try:
    from hashlib import sha1
except ImportError:
    from sha import new as sha1
    
sha1_teste = '2e6f9b0d5885b6010f9167787445617f553a735f'
print version_info
s = sha1('teste')
print s.hexdigest()
if s.hexdigest() == sha1_teste:
    print 'OK'
else:
    print 'Erro'
    print sha1_teste
    print s