#!/usr/bin/env python
# coding: cp1252

import sys
from time import time
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

class Cronometro(QDialog):
    
    def __init__(self):
        super(Cronometro, self).__init__()
        self.visor = QLabel('<h1>00.00</h1>')
        self.visor.setMargin(10)
        self.btIniciar = QPushButton('Iniciar')
        self.btZerar = QPushButton('Zerar')
        layout = QGridLayout()
        layout.addWidget(self.visor,0,0,1,2)
        layout.addWidget(self.btIniciar,1,0)
        layout.addWidget(self.btZerar,1,1)
        self.setLayout(layout)
        self.setWindowTitle('Cronômetro')
        self.connect(self.btIniciar,
                SIGNAL("clicked()"), self.iniciar)
        self.connect(self.btZerar,
                SIGNAL("clicked()"), self.zerar)
        self.inicio = None
        self.timer = None
        
    def iniciar(self):
        if self.timer is None:
            if self.inicio is None:
                self.inicio = time()
            self.btIniciar.setText('Parar')
            self.timer = self.startTimer(10)
        else:
            self.killTimer(self.timer)
            self.timer = None
            self.btIniciar.setText('Iniciar')

    def zerar(self):
        self.visor.setText('<h1>00.00</h1>')
        self.inicio = None
        if self.timer:
            self.killTimer(self.timer)
            self.timer = None    

    def timerEvent(self, event):
        agora = time()
        segs = round(agora-self.inicio,2)
        tempo = '<h1>%05.2f</h1>' % (segs)
        self.visor.setText(tempo)

app = QApplication(sys.argv)
crono = Cronometro()
crono.show()
app.exec_()

