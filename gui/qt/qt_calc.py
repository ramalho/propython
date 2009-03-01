#!/usr/bin/env python
# coding: cp1252

# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from __future__ import division
import sys
from math import *
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

class Form(QDialog):
    
    valor = 0

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit('Digite uma expressão e tecle [ENTER]')
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect(self.lineedit, SIGNAL("returnPressed()"),
                     self.updateUi)
        self.setWindowTitle("Calculadora")
        

    def updateUi(self):
        try:
            text = unicode(self.lineedit.text())
            self.valor = eval(text, globals(), {'z':self.valor})
            self.browser.append("%s = <b>%s</b>" % (text, self.valor))
        except:
            self.browser.append(
                    "<font color=red>%s is invalid!</font>" % text)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

