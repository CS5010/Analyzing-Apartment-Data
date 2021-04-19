# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotWidget(object):
    def setupUi(self, PlotWidget):
        PlotWidget.setObjectName("PlotWidget")
        PlotWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(PlotWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plot_label_plot_type = QtWidgets.QLabel(PlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_label_plot_type.sizePolicy().hasHeightForWidth())
        self.plot_label_plot_type.setSizePolicy(sizePolicy)
        self.plot_label_plot_type.setObjectName("plot_label_plot_type")
        self.horizontalLayout_2.addWidget(self.plot_label_plot_type)
        self.plot_cb_plot_type = QtWidgets.QComboBox(PlotWidget)
        self.plot_cb_plot_type.setObjectName("plot_cb_plot_type")
        self.horizontalLayout_2.addWidget(self.plot_cb_plot_type)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.plot_stacked_widget = QtWidgets.QStackedWidget(PlotWidget)
        self.plot_stacked_widget.setObjectName("plot_stacked_widget")
        self.verticalLayout.addWidget(self.plot_stacked_widget)
        self.plot_btn_plot = QtWidgets.QPushButton(PlotWidget)
        self.plot_btn_plot.setObjectName("plot_btn_plot")
        self.verticalLayout.addWidget(self.plot_btn_plot)

        self.retranslateUi(PlotWidget)
        QtCore.QMetaObject.connectSlotsByName(PlotWidget)

    def retranslateUi(self, PlotWidget):
        _translate = QtCore.QCoreApplication.translate
        PlotWidget.setWindowTitle(_translate("PlotWidget", "Form"))
        self.plot_label_plot_type.setText(_translate("PlotWidget", "Plot Type"))
        self.plot_btn_plot.setText(_translate("PlotWidget", "Plot"))

