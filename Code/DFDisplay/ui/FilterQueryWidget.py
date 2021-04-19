# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterQueryWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterQueryWidget(object):
    def setupUi(self, FilterQueryWidget):
        FilterQueryWidget.setObjectName("FilterQueryWidget")
        FilterQueryWidget.resize(400, 66)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FilterQueryWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_columns = QtWidgets.QComboBox(FilterQueryWidget)
        self.cb_columns.setObjectName("cb_columns")
        self.horizontalLayout.addWidget(self.cb_columns)
        self.cb_operations = QtWidgets.QComboBox(FilterQueryWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_operations.sizePolicy().hasHeightForWidth())
        self.cb_operations.setSizePolicy(sizePolicy)
        self.cb_operations.setObjectName("cb_operations")
        self.cb_operations.addItem("")
        self.cb_operations.addItem("")
        self.cb_operations.addItem("")
        self.cb_operations.addItem("")
        self.cb_operations.addItem("")
        self.horizontalLayout.addWidget(self.cb_operations)
        self.txt_target_val = QtWidgets.QLineEdit(FilterQueryWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_target_val.sizePolicy().hasHeightForWidth())
        self.txt_target_val.setSizePolicy(sizePolicy)
        self.txt_target_val.setObjectName("txt_target_val")
        self.horizontalLayout.addWidget(self.txt_target_val)

        self.retranslateUi(FilterQueryWidget)
        QtCore.QMetaObject.connectSlotsByName(FilterQueryWidget)

    def retranslateUi(self, FilterQueryWidget):
        _translate = QtCore.QCoreApplication.translate
        FilterQueryWidget.setWindowTitle(_translate("FilterQueryWidget", "Form"))
        self.cb_operations.setItemText(0, _translate("FilterQueryWidget", "="))
        self.cb_operations.setItemText(1, _translate("FilterQueryWidget", "<"))
        self.cb_operations.setItemText(2, _translate("FilterQueryWidget", "<="))
        self.cb_operations.setItemText(3, _translate("FilterQueryWidget", ">"))
        self.cb_operations.setItemText(4, _translate("FilterQueryWidget", ">="))

