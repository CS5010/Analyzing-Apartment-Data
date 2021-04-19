# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterWidget(object):
    def setupUi(self, FilterWidget):
        FilterWidget.setObjectName("FilterWidget")
        FilterWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter_actions_label = QtWidgets.QLabel(FilterWidget)
        self.filter_actions_label.setObjectName("filter_actions_label")
        self.horizontalLayout.addWidget(self.filter_actions_label)
        self.filter_actions_cb = QtWidgets.QComboBox(FilterWidget)
        self.filter_actions_cb.setObjectName("filter_actions_cb")
        self.horizontalLayout.addWidget(self.filter_actions_cb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filter_stacked_widget = QtWidgets.QStackedWidget(FilterWidget)
        self.filter_stacked_widget.setObjectName("filter_stacked_widget")
        self.verticalLayout.addWidget(self.filter_stacked_widget)
        self.filter_btn_submit = QtWidgets.QPushButton(FilterWidget)
        self.filter_btn_submit.setObjectName("filter_btn_submit")
        self.verticalLayout.addWidget(self.filter_btn_submit)

        self.retranslateUi(FilterWidget)
        QtCore.QMetaObject.connectSlotsByName(FilterWidget)

    def retranslateUi(self, FilterWidget):
        _translate = QtCore.QCoreApplication.translate
        FilterWidget.setWindowTitle(_translate("FilterWidget", "Form"))
        self.filter_actions_label.setText(_translate("FilterWidget", "Filter action"))
        self.filter_btn_submit.setText(_translate("FilterWidget", "Filter"))

