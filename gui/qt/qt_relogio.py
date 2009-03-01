#!/usr/bin/env python
# coding: cp1252

import sys
from datetime import datetime
from PyQt4.QtGui import *

class Relogio(QLabel):
    
    def __init__(self):
        super(Relogio, self).__init__()
        self.setMargin(10)
        self.setText(self.hora()) 
        self.setWindowTitle('Relógio')
        self.startTimer(10)
        
    def hora(self):
        return datetime.now().strftime('<h1>%H:%M:%S</h1>')

    def timerEvent(self, event):
        self.setText(self.hora())

app = QApplication(sys.argv)
relogio = Relogio()
relogio.show()
app.exec_()

