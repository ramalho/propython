#!/usr/bin/env python
# coding: cp1252

import sys
from PyQt4.QtGui import *

class Calendario(QCalendarWidget):
    
    def __init__(self):
        super(Calendario, self).__init__()
        self.setWindowTitle('Calendário')
        
app = QApplication(sys.argv)
calendario = Calendario()
calendario.show()
app.exec_()

