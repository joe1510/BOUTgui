# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanbout.ui'
#
# Created: Thu Aug 20 18:30:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

"""
BOUT gui is designed as a graphical interface for running BOUT++ simulations
    Copyright (C) 2015 authored by Joseph Henderson, Department of Physics, York, jh1479@york.ac.uk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
from PySide import QtCore, QtGui

class Ui_ScanDialog(object):
    def setupUi(self, ScanDialog):
        ScanDialog.setObjectName("ScanDialog")
        ScanDialog.resize(393, 409)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BOUTguilogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScanDialog.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(ScanDialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 363, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(ScanDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 363, 75, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtGui.QGroupBox(ScanDialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 331, 121))
        self.groupBox.setObjectName("groupBox")
        self.incrementLine = QtGui.QLineEdit(self.groupBox)
        self.incrementLine.setGeometry(QtCore.QRect(240, 90, 81, 21))
        self.incrementLine.setObjectName("incrementLine")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(240, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.indexCombo = QtGui.QComboBox(self.groupBox)
        self.indexCombo.setGeometry(QtCore.QRect(170, 40, 151, 22))
        self.indexCombo.setObjectName("indexCombo")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 56, 15))
        self.label.setObjectName("label")
        self.finalLine = QtGui.QLineEdit(self.groupBox)
        self.finalLine.setGeometry(QtCore.QRect(124, 90, 81, 21))
        self.finalLine.setObjectName("finalLine")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 56, 15))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(124, 70, 71, 16))
        self.label_4.setObjectName("label_4")
        self.initialLine = QtGui.QLineEdit(self.groupBox)
        self.initialLine.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.initialLine.setObjectName("initialLine")
        self.sectionCombo = QtGui.QComboBox(self.groupBox)
        self.sectionCombo.setGeometry(QtCore.QRect(10, 40, 151, 22))
        self.sectionCombo.setObjectName("sectionCombo")
        self.groupBox_3 = QtGui.QGroupBox(ScanDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 140, 331, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.sectionCombo_2 = QtGui.QComboBox(self.groupBox_3)
        self.sectionCombo_2.setGeometry(QtCore.QRect(10, 40, 151, 22))
        self.sectionCombo_2.setObjectName("sectionCombo_2")
        self.indexCombo_2 = QtGui.QComboBox(self.groupBox_3)
        self.indexCombo_2.setGeometry(QtCore.QRect(170, 40, 151, 22))
        self.indexCombo_2.setObjectName("indexCombo_2")
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 56, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(170, 20, 56, 15))
        self.label_10.setObjectName("label_10")
        self.finalLine2 = QtGui.QLineEdit(self.groupBox_3)
        self.finalLine2.setGeometry(QtCore.QRect(124, 90, 81, 21))
        self.finalLine2.setObjectName("finalLine2")
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_7.setObjectName("label_7")
        self.initialLine2 = QtGui.QLineEdit(self.groupBox_3)
        self.initialLine2.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.initialLine2.setObjectName("initialLine2")
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(240, 70, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(124, 70, 81, 16))
        self.label_8.setObjectName("label_8")
        self.incrementLine2 = QtGui.QLineEdit(self.groupBox_3)
        self.incrementLine2.setGeometry(QtCore.QRect(240, 90, 81, 21))
        self.incrementLine2.setObjectName("incrementLine2")
        self.groupBox_2 = QtGui.QGroupBox(ScanDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 270, 331, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(8, 20, 91, 16))
        self.label_12.setObjectName("label_12")
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(108, 48, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(108, 18, 211, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(8, 50, 91, 16))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(ScanDialog)
        QtCore.QMetaObject.connectSlotsByName(ScanDialog)

    def retranslateUi(self, ScanDialog):
        ScanDialog.setWindowTitle(QtGui.QApplication.translate("ScanDialog", "Scanning Simulation Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ScanDialog", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ScanDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ScanDialog", "First Variable to Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ScanDialog", "Initial Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ScanDialog", "Increment", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ScanDialog", "Section", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScanDialog", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ScanDialog", "Final Value", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ScanDialog", "Second Variable to Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ScanDialog", "Section", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ScanDialog", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ScanDialog", "Initial Value 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ScanDialog", "Increment 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ScanDialog", "Final Value 2", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ScanDialog", "Other Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ScanDialog", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("ScanDialog", "Simultaneous Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("ScanDialog", "Full Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("ScanDialog", "Percentage", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("ScanDialog", "Raw", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ScanDialog", "Scan Mode:", None, QtGui.QApplication.UnicodeUTF8))

