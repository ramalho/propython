#!/usr/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime
from time import sleep

while True:    # rodar para sempre 
    hora = datetime.now()
    print hora.strftime('%H:%M:%S') 
    sleep(1)   # aguardar 1 segundo
