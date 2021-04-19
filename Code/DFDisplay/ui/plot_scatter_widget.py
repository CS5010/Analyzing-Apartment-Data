# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_scatter_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plot_scatter_widget(object):
    def setupUi(self, plot_scatter_widget):
        plot_scatter_widget.setObjectName("plot_scatter_widget")
        plot_scatter_widget.resize(400, 237)
        self.verticalLayout = QtWidgets.QVBoxLayout(plot_scatter_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scatter_label_title = QtWidgets.QLabel(plot_scatter_widget)
        self.scatter_label_title.setObjectName("scatter_label_title")
        self.horizontalLayout_3.addWidget(self.scatter_label_title)
        self.scatter_line_title = QtWidgets.QLineEdit(plot_scatter_widget)
        self.scatter_line_title.setObjectName("scatter_line_title")
        self.horizontalLayout_3.addWidget(self.scatter_line_title)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scatter_label_x = QtWidgets.QLabel(plot_scatter_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_label_x.sizePolicy().hasHeightForWidth())
        self.scatter_label_x.setSizePolicy(sizePolicy)
        self.scatter_label_x.setObjectName("scatter_label_x")
        self.horizontalLayout.addWidget(self.scatter_label_x)
        self.scatter_cb_x = QtWidgets.QComboBox(plot_scatter_widget)
        self.scatter_cb_x.setObjectName("scatter_cb_x")
        self.horizontalLayout.addWidget(self.scatter_cb_x)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scatter_label_y = QtWidgets.QLabel(plot_scatter_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_label_y.sizePolicy().hasHeightForWidth())
        self.scatter_label_y.setSizePolicy(sizePolicy)
        self.scatter_label_y.setObjectName("scatter_label_y")
        self.horizontalLayout_2.addWidget(self.scatter_label_y)
        self.scatter_cb_y = QtWidgets.QComboBox(plot_scatter_widget)
        self.scatter_cb_y.setObjectName("scatter_cb_y")
        self.horizontalLayout_2.addWidget(self.scatter_cb_y)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(plot_scatter_widget)
        QtCore.QMetaObject.connectSlotsByName(plot_scatter_widget)

    def retranslateUi(self, plot_scatter_widget):
        _translate = QtCore.QCoreApplication.translate
        plot_scatter_widget.setWindowTitle(_translate("plot_scatter_widget", "Form"))
        self.scatter_label_title.setText(_translate("plot_scatter_widget", "Plot Title"))
        self.scatter_label_x.setText(_translate("plot_scatter_widget", "x variable"))
        self.scatter_label_y.setText(_translate("plot_scatter_widget", "y variable"))

