# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stupidsheet.ui'
#
# Created: Sat Nov  1 07:49:23 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid = QtGui.QTableWidget(Form)
        self.grid.setObjectName("grid")
        self.grid.setColumnCount(10)
        self.grid.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.grid.setHorizontalHeaderItem(9, item)
        self.verticalLayout.addWidget(self.grid)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Form", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Form", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("Form", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("Form", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("Form", "J", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

