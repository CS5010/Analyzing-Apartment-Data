# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:30:16 2020

@author: Dave
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ui.PlotWidget import Ui_PlotWidget
from ui.plot_scatter_widget import Ui_plot_scatter_widget
from ui.plot_bar_widget import Ui_plot_bar_widget

class PlotWidget(QWidget,Ui_PlotWidget):
    """
    Widget in the main stacked widget used to host plot type subwidgets and process their info
    """
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.make_connections()
        self.add_sub_widget(ScatterWidget(self),"Scatter")
        self.add_sub_widget(BarWidget(self),"Bar")
        
    def make_connections(self):
        """
        Connect actions to functions
        """
        self.plot_btn_plot.clicked.connect(self.call_plot)
        self.plot_cb_plot_type.currentIndexChanged.connect(self.swap_plot_type_widgets)
    
    
    def add_sub_widget(self, widget, label):
        """
        Add plot subtype widgets to the stackedwidget within this widget
        Parameters
        ----------
        widget : pyqt widget
            The subwidget to embed.
        label : String
            The label to display in the combobox fo the added widget.

        Returns
        -------
        None.

        """
        self.plot_stacked_widget.addWidget(widget)
        self.plot_cb_plot_type.addItems([label])
        
    def call_plot(self): 
        """
        Requests the plot dictionary from the currently active subwidget
        Then passes the dictionary to dfdisplays plot function
        Returns
        -------
        None.
        """
        plot_dict = self.plot_stacked_widget.currentWidget().get_plot_dict()
        self.parent.plot(plot_dict)
    
    def swap_plot_type_widgets(self):
        self.plot_stacked_widget.setCurrentIndex(self.plot_cb_plot_type.currentIndex())
        
    def update_available_columns(self,data_frame):
        """
        Pass the dataframe to each subwidget so they can populate their dropdowns of columns
        """
        num_widgets = self.plot_stacked_widget.count()
        for idx in range(num_widgets):
            widget = self.plot_stacked_widget.widget(idx)
            widget.update_available_columns(data_frame)
    
        
class ScatterWidget(QWidget, Ui_plot_scatter_widget):
    """
    Widget for gathering information from the user for building a scatterplot
    """
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        
    def update_available_columns(self, data_frame):
        """
        Pull in a list of available columns in the dataframe
        """
        col_list = data_frame.columns.to_list()
        col_list.sort()
        self.scatter_cb_x.clear()
        self.scatter_cb_x.addItems(col_list)
        self.scatter_cb_y.clear()
        self.scatter_cb_y.addItems(col_list)
    
    def get_plot_dict(self):
        """
        Build a dictionary of user specified options that can be used to build the plot
        """
        plot_dict ={"mode" : "scatter",
                    "data" : {},
                    "options":{}
                    }
        plot_dict["data"]["x_data"] = self.scatter_cb_x.currentText()
        plot_dict["data"]["y_data"] = self.scatter_cb_y.currentText()
        title = self.scatter_line_title.text()
        if not title: #if empty string
            title = "Plot of {0} vs {1}".format( plot_dict["data"]["x_data"],plot_dict["data"]["y_data"])
        plot_dict["options"]["title"] = title
        return plot_dict

class BarWidget(QWidget, Ui_plot_bar_widget):
    """
    Widget for gathering information from the user for building a scatterplot
    """
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
    
    def update_available_columns(self, data_frame):
        """
        Pull in a list of available columns in the dataframe
        """
        col_list = data_frame.columns.to_list()
        col_list.sort()
        self.bar_cb_count.clear()
        self.bar_cb_count.addItems(col_list)
        self.bar_cb_families.clear()
        self.bar_cb_families.addItems(["None"])
        self.bar_cb_families.addItems(col_list)
        
    def get_plot_dict(self):
        """
        Build a dictionary of user specified options that can be used to build the plot
        """
        plot_dict ={"mode" : "bar",
                    "data" : {},
                    "options":{}
                    }
        plot_dict["data"]["count"] = self.bar_cb_count.currentText()
        plot_dict["data"]["families"] = self.bar_cb_families.currentText()
        plot_dict["options"]["percentage"]= self.bar_box_percentage.isChecked()
        plot_dict["options"]["stacked"]= self.bar_box_stacked.isChecked()
        return plot_dict