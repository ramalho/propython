#!/usr/bin/env python
# coding: cp1252

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL

class Botao(QPushButton):
    
    def __init__(self):
        super(Botao, self).__init__()
        self.setText('Aperte-me')
        self.setWindowTitle('Botão')
        self.connect(self, SIGNAL("clicked()"), self.clicado)

    def clicado(self):
        if self.text() == 'Aperte-me':
            self.setText('Grato!')
        else:
            self.setText('Aperte-me')
        
app = QApplication(sys.argv)
btn = Botao()
btn.show()
app.exec_()

