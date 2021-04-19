# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterHistoryWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterHistoryWidget(object):
    def setupUi(self, FilterHistoryWidget):
        FilterHistoryWidget.setObjectName("FilterHistoryWidget")
        FilterHistoryWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterHistoryWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filt_history_label_title = QtWidgets.QLabel(FilterHistoryWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filt_history_label_title.sizePolicy().hasHeightForWidth())
        self.filt_history_label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.filt_history_label_title.setFont(font)
        self.filt_history_label_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.filt_history_label_title.setObjectName("filt_history_label_title")
        self.verticalLayout.addWidget(self.filt_history_label_title)
        self.filt_history_label_history = QtWidgets.QLabel(FilterHistoryWidget)
        self.filt_history_label_history.setText("")
        self.filt_history_label_history.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.filt_history_label_history.setObjectName("filt_history_label_history")
        self.verticalLayout.addWidget(self.filt_history_label_history)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(FilterHistoryWidget)
        QtCore.QMetaObject.connectSlotsByName(FilterHistoryWidget)

    def retranslateUi(self, FilterHistoryWidget):
        _translate = QtCore.QCoreApplication.translate
        FilterHistoryWidget.setWindowTitle(_translate("FilterHistoryWidget", "Form"))
        self.filt_history_label_title.setText(_translate("FilterHistoryWidget", "FILTER HISTORY"))

