# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resize.ui'
#
# Created: Thu Aug 20 18:29:31 2015
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

class Ui_Resize(object):
    def setupUi(self, Resize):
        Resize.setObjectName("Resize")
        Resize.resize(283, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BOUTguilogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Resize.setWindowIcon(icon)
        self.ok = QtGui.QPushButton(Resize)
        self.ok.setGeometry(QtCore.QRect(40, 250, 75, 25))
        self.ok.setObjectName("ok")
        self.cancel = QtGui.QPushButton(Resize)
        self.cancel.setGeometry(QtCore.QRect(116, 250, 75, 25))
        self.cancel.setObjectName("cancel")
        self.apply = QtGui.QPushButton(Resize)
        self.apply.setGeometry(QtCore.QRect(193, 250, 75, 25))
        self.apply.setObjectName("apply")
        self.groupBox = QtGui.QGroupBox(Resize)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 231))
        self.groupBox.setObjectName("groupBox")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 197, 161, 16))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 23, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 176, 111, 16))
        self.label_6.setObjectName("label_6")
        self.leftSpin = QtGui.QSpinBox(self.groupBox)
        self.leftSpin.setGeometry(QtCore.QRect(150, 40, 101, 22))
        self.leftSpin.setMaximum(10000)
        self.leftSpin.setObjectName("leftSpin")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 77, 131, 16))
        self.label_2.setObjectName("label_2")
        self.inputSepSpin = QtGui.QSpinBox(self.groupBox)
        self.inputSepSpin.setGeometry(QtCore.QRect(150, 95, 101, 22))
        self.inputSepSpin.setMaximum(10000)
        self.inputSepSpin.setObjectName("inputSepSpin")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 45, 111, 16))
        self.label.setObjectName("label")
        self.widthSpin = QtGui.QSpinBox(self.groupBox)
        self.widthSpin.setGeometry(QtCore.QRect(150, 173, 101, 22))
        self.widthSpin.setMaximum(10000)
        self.widthSpin.setObjectName("widthSpin")
        self.vSpin = QtGui.QSpinBox(self.groupBox)
        self.vSpin.setGeometry(QtCore.QRect(150, 73, 101, 22))
        self.vSpin.setMaximum(10000)
        self.vSpin.setObjectName("vSpin")
        self.maxSpin = QtGui.QSpinBox(self.groupBox)
        self.maxSpin.setGeometry(QtCore.QRect(150, 129, 101, 22))
        self.maxSpin.setMaximum(10000)
        self.maxSpin.setObjectName("maxSpin")
        self.topSpin = QtGui.QSpinBox(self.groupBox)
        self.topSpin.setGeometry(QtCore.QRect(150, 18, 101, 22))
        self.topSpin.setMaximum(10000)
        self.topSpin.setObjectName("topSpin")
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 97, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 133, 131, 16))
        self.label_4.setObjectName("label_4")
        self.hSpin = QtGui.QSpinBox(self.groupBox)
        self.hSpin.setGeometry(QtCore.QRect(150, 195, 101, 22))
        self.hSpin.setMaximum(10000)
        self.hSpin.setObjectName("hSpin")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 155, 131, 16))
        self.label_5.setObjectName("label_5")
        self.boxLengthSpin = QtGui.QSpinBox(self.groupBox)
        self.boxLengthSpin.setGeometry(QtCore.QRect(150, 151, 101, 22))
        self.boxLengthSpin.setMaximum(10000)
        self.boxLengthSpin.setObjectName("boxLengthSpin")

        self.retranslateUi(Resize)
        QtCore.QMetaObject.connectSlotsByName(Resize)

    def retranslateUi(self, Resize):
        Resize.setWindowTitle(QtGui.QApplication.translate("Resize", "Resize and Reposition", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("Resize", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Resize", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.apply.setText(QtGui.QApplication.translate("Resize", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Resize", "Size and Position Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Resize", "Horizontal Separation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Resize", "Top Border", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Resize", "Box Width", None, QtGui.QApplication.UnicodeUTF8))
        self.leftSpin.setToolTip(QtGui.QApplication.translate("Resize", "change the left side of the border bewteen the mainwindow and the first boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Resize", "Vertical Separation", None, QtGui.QApplication.UnicodeUTF8))
        self.inputSepSpin.setToolTip(QtGui.QApplication.translate("Resize", "Change the gap between the input controls", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Resize", "Left Border", None, QtGui.QApplication.UnicodeUTF8))
        self.widthSpin.setToolTip(QtGui.QApplication.translate("Resize", "change the width of the boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.vSpin.setToolTip(QtGui.QApplication.translate("Resize", "change the vertical seperation between the boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.maxSpin.setToolTip(QtGui.QApplication.translate("Resize", "change the limit of the length of each column of boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.topSpin.setToolTip(QtGui.QApplication.translate("Resize", "change the top side of the border bewteen the mainwindow and the first boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Resize", "Input Separation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Resize", "Length of Scrolling", None, QtGui.QApplication.UnicodeUTF8))
        self.hSpin.setToolTip(QtGui.QApplication.translate("Resize", "Chagne the horizontal seperation between the boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Resize", "Box Length", None, QtGui.QApplication.UnicodeUTF8))
        self.boxLengthSpin.setToolTip(QtGui.QApplication.translate("Resize", "change the limit of the length of each column of boxes", None, QtGui.QApplication.UnicodeUTF8))

