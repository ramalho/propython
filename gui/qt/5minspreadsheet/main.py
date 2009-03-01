#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pythonbrazil.org"""

# Imports típicos
import os,sys

# Importamos los módulos Qt
from PyQt4 import QtCore,QtGui

# Importamos el módulo generado por pyuic (podríamos cargar 
# directamente el XML)
from sheetUi import Ui_Form


class SpreadSheet:
    _cells = {}
    tools = {}
    def __setitem__(self, key, formula):
        self._cells[key] = formula
    def getformula(self, key):
        return self._cells[key]
    def __getitem__(self, key ):
        return eval(self._cells[key], SpreadSheet.tools, self)

# Creamos una clase para nuestra ventana principal
class Main(QtGui.QWidget):
    def __init__(self):
        # Si, ya sé que tendría que usar super()
        QtGui.QWidget.__init__(self)
        
        # Esto es siempre EXACTAMENTE igual
        self.ui=Ui_Form()
        self.ui.setupUi(self)
	self.sheet=SpreadSheet()
	import math
	self.sheet.tools=math
	QtCore.QObject.connect(self.ui.grid,QtCore.SIGNAL("cellChanged(int,int)"),
	    self.calculateCell)

    def calculateCell(self,row,column):
	# Si no desconecto, cuando calculo la celda llama a calculateCell (maxdepth recursion!)
	QtCore.QObject.disconnect(self.ui.grid,QtCore.SIGNAL("cellChanged(int,int)"),
	    self.calculateCell)
	try: # Puede fallar!

	    # Convierto 1,3 en A3
	    cellname=chr(ord("A")+column)+str(row+1)
	    # O mejor: a3
	    cellname=cellname.lower()

	    # Saco la formula de grid
	    formula=unicode(self.ui.grid.item(row,column).text()).lower()
	    
	    # Asigno la formula a la celda correspondiente en sheet
	    self.sheet[cellname]=formula

	    # Tomamos el resultado y lo ponemos en la celda
	    self.ui.grid.setItem(row,column,QtGui.QTableWidgetItem(str(self.sheet[cellname])))
	except:
	    pass

	# Reconectamos para que la proxima celda tambien se pueda calcular
	QtCore.QObject.connect(self.ui.grid,QtCore.SIGNAL("cellChanged(int,int)"),
	    self.calculateCell)


def main():
    # De nuevo, esto es "boilerplate", es igual en todas las aplicaciones
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # Es exec_ porque exec es reservada en python
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()