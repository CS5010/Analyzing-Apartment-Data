# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_bar_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plot_bar_widget(object):
    def setupUi(self, plot_bar_widget):
        plot_bar_widget.setObjectName("plot_bar_widget")
        plot_bar_widget.resize(400, 237)
        self.verticalLayout = QtWidgets.QVBoxLayout(plot_bar_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bar_label_count = QtWidgets.QLabel(plot_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar_label_count.sizePolicy().hasHeightForWidth())
        self.bar_label_count.setSizePolicy(sizePolicy)
        self.bar_label_count.setObjectName("bar_label_count")
        self.horizontalLayout.addWidget(self.bar_label_count)
        self.bar_cb_count = QtWidgets.QComboBox(plot_bar_widget)
        self.bar_cb_count.setObjectName("bar_cb_count")
        self.horizontalLayout.addWidget(self.bar_cb_count)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bar_label_families = QtWidgets.QLabel(plot_bar_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar_label_families.sizePolicy().hasHeightForWidth())
        self.bar_label_families.setSizePolicy(sizePolicy)
        self.bar_label_families.setObjectName("bar_label_families")
        self.horizontalLayout_2.addWidget(self.bar_label_families)
        self.bar_cb_families = QtWidgets.QComboBox(plot_bar_widget)
        self.bar_cb_families.setObjectName("bar_cb_families")
        self.horizontalLayout_2.addWidget(self.bar_cb_families)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bar_box_percentage = QtWidgets.QCheckBox(plot_bar_widget)
        self.bar_box_percentage.setObjectName("bar_box_percentage")
        self.horizontalLayout_3.addWidget(self.bar_box_percentage)
        self.bar_box_stacked = QtWidgets.QCheckBox(plot_bar_widget)
        self.bar_box_stacked.setObjectName("bar_box_stacked")
        self.horizontalLayout_3.addWidget(self.bar_box_stacked)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(plot_bar_widget)
        QtCore.QMetaObject.connectSlotsByName(plot_bar_widget)

    def retranslateUi(self, plot_bar_widget):
        _translate = QtCore.QCoreApplication.translate
        plot_bar_widget.setWindowTitle(_translate("plot_bar_widget", "Form"))
        self.bar_label_count.setText(_translate("plot_bar_widget", "Count Variable:"))
        self.bar_label_families.setText(_translate("plot_bar_widget", "Families:"))
        self.bar_box_percentage.setText(_translate("plot_bar_widget", "As Percentage"))
        self.bar_box_stacked.setText(_translate("plot_bar_widget", "Stacked Bars"))

