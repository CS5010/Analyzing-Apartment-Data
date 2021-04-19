# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileOpenCSVWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_file_open_csv_widget(object):
    def setupUi(self, file_open_csv_widget):
        file_open_csv_widget.setObjectName("file_open_csv_widget")
        file_open_csv_widget.resize(487, 153)
        self.verticalLayout = QtWidgets.QVBoxLayout(file_open_csv_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_btn_open = QtWidgets.QPushButton(file_open_csv_widget)
        self.file_btn_open.setObjectName("file_btn_open")
        self.horizontalLayout.addWidget(self.file_btn_open)
        self.file_txt_filename = QtWidgets.QLineEdit(file_open_csv_widget)
        self.file_txt_filename.setEnabled(False)
        self.file_txt_filename.setObjectName("file_txt_filename")
        self.horizontalLayout.addWidget(self.file_txt_filename)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file_label_separator = QtWidgets.QLabel(file_open_csv_widget)
        self.file_label_separator.setObjectName("file_label_separator")
        self.horizontalLayout_2.addWidget(self.file_label_separator)
        self.file_txt_sep = QtWidgets.QLineEdit(file_open_csv_widget)
        self.file_txt_sep.setObjectName("file_txt_sep")
        self.horizontalLayout_2.addWidget(self.file_txt_sep)
        self.file_label_encoding = QtWidgets.QLabel(file_open_csv_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_label_encoding.sizePolicy().hasHeightForWidth())
        self.file_label_encoding.setSizePolicy(sizePolicy)
        self.file_label_encoding.setObjectName("file_label_encoding")
        self.horizontalLayout_2.addWidget(self.file_label_encoding)
        self.file_cb_encoding = QtWidgets.QComboBox(file_open_csv_widget)
        self.file_cb_encoding.setObjectName("file_cb_encoding")
        self.file_cb_encoding.addItem("")
        self.file_cb_encoding.addItem("")
        self.horizontalLayout_2.addWidget(self.file_cb_encoding)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.file_btn_loadcsv = QtWidgets.QPushButton(file_open_csv_widget)
        self.file_btn_loadcsv.setObjectName("file_btn_loadcsv")
        self.horizontalLayout_3.addWidget(self.file_btn_loadcsv)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(file_open_csv_widget)
        QtCore.QMetaObject.connectSlotsByName(file_open_csv_widget)

    def retranslateUi(self, file_open_csv_widget):
        _translate = QtCore.QCoreApplication.translate
        file_open_csv_widget.setWindowTitle(_translate("file_open_csv_widget", "Form"))
        self.file_btn_open.setText(_translate("file_open_csv_widget", "Open"))
        self.file_label_separator.setText(_translate("file_open_csv_widget", "Separator"))
        self.file_txt_sep.setText(_translate("file_open_csv_widget", ","))
        self.file_label_encoding.setText(_translate("file_open_csv_widget", "Encoding"))
        self.file_cb_encoding.setItemText(0, _translate("file_open_csv_widget", "UTF-8"))
        self.file_cb_encoding.setItemText(1, _translate("file_open_csv_widget", "ANSI"))
        self.file_btn_loadcsv.setText(_translate("file_open_csv_widget", "Load CSV"))

