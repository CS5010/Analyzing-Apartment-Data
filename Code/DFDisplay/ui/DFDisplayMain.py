# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DFDisplayMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.display_frame_plot = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_frame_plot.sizePolicy().hasHeightForWidth())
        self.display_frame_plot.setSizePolicy(sizePolicy)
        self.display_frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display_frame_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display_frame_plot.setObjectName("display_frame_plot")
        self.horizontalLayout_2.addWidget(self.display_frame_plot)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.disp_label_number_rows = QtWidgets.QLabel(self.centralwidget)
        self.disp_label_number_rows.setObjectName("disp_label_number_rows")
        self.verticalLayout.addWidget(self.disp_label_number_rows)
        self.dispaly_horizontalLayout_widget_selection = QtWidgets.QHBoxLayout()
        self.dispaly_horizontalLayout_widget_selection.setObjectName("dispaly_horizontalLayout_widget_selection")
        self.display_label_cur_wdiget = QtWidgets.QLabel(self.centralwidget)
        self.display_label_cur_wdiget.setObjectName("display_label_cur_wdiget")
        self.dispaly_horizontalLayout_widget_selection.addWidget(self.display_label_cur_wdiget)
        self.display_cb_select_widget = QtWidgets.QComboBox(self.centralwidget)
        self.display_cb_select_widget.setObjectName("display_cb_select_widget")
        self.dispaly_horizontalLayout_widget_selection.addWidget(self.display_cb_select_widget)
        self.verticalLayout.addLayout(self.dispaly_horizontalLayout_widget_selection)
        self.display_stackedWidget_tools = QtWidgets.QStackedWidget(self.centralwidget)
        self.display_stackedWidget_tools.setObjectName("display_stackedWidget_tools")
        self.verticalLayout.addWidget(self.display_stackedWidget_tools)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.display_btn_undo = QtWidgets.QPushButton(self.centralwidget)
        self.display_btn_undo.setObjectName("display_btn_undo")
        self.horizontalLayout.addWidget(self.display_btn_undo)
        self.display_btn_redo = QtWidgets.QPushButton(self.centralwidget)
        self.display_btn_redo.setObjectName("display_btn_redo")
        self.horizontalLayout.addWidget(self.display_btn_redo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_CSV = QtWidgets.QAction(MainWindow)
        self.actionOpen_CSV.setObjectName("actionOpen_CSV")
        self.actionSave_Plot = QtWidgets.QAction(MainWindow)
        self.actionSave_Plot.setObjectName("actionSave_Plot")
        self.menuFile.addAction(self.actionOpen_CSV)
        self.menuFile.addAction(self.actionSave_Plot)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.disp_label_number_rows.setText(_translate("MainWindow", "No dataframe loaded"))
        self.display_label_cur_wdiget.setText(_translate("MainWindow", "Tool Panel:"))
        self.display_btn_undo.setText(_translate("MainWindow", "Undo"))
        self.display_btn_redo.setText(_translate("MainWindow", "Redo"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_CSV.setText(_translate("MainWindow", "Open CSV"))
        self.actionSave_Plot.setText(_translate("MainWindow", "Save Plot"))

