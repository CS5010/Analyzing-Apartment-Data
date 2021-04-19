# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:07:03 2020

@author: Dave
"""
import sys
import os
import pandas as pd
import numpy as np
import path
from operator import add
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import pyqtgraph as pg
from ui import DFDisplayMain, FileOpenCSVWidget
from filter.FilterWidgets import FilterWidget
from plot.PlotTools import PlotWidget

class DFMainWindow(QMainWindow,DFDisplayMain.Ui_MainWindow):
    
    def __init__(self):
        #Initialize all the embedded widgets that make up the application
        super().__init__()
        self.setupUi(self)
        self.filter_widget = FilterWidget(parent=self)
        self.tools_plot_widget = PlotWidget(parent=self)
        self._add_widget(self.filter_widget, "filter")
        self._add_widget(self.tools_plot_widget, "plot")
        self.file_open_widget = FileOpenCSVWidget(self)
        vbox = QVBoxLayout()
        self.graph = MplCanvas(self)
        vbox.addWidget(self.graph)
        self.display_frame_plot.setLayout(vbox)
        self.data_frame = None
        self.current_data_frame = None
        self.queries = []
        self.current_query_location = 0
        self.make_connections()
        self.update_gui_info()
    
    def _add_widget(self, widget, text):
        #Adds the passed widget to the right side stacked widget pane and pairs it 
        #With the specified text in the combo box above the stackedwidget
        self.display_stackedWidget_tools.addWidget(widget)
        self.display_cb_select_widget.addItem(text)
        
    def make_connections(self):
        #Connect the buttons to their respective functions
        self.display_btn_undo.clicked.connect(self.undo_query)
        self.display_btn_redo.clicked.connect(self.redo_query)
        self.actionOpen_CSV.triggered.connect(self.file_open_widget.show)
        self.actionSave_Plot.triggered.connect(self.save_plot)
        self.display_cb_select_widget.currentIndexChanged.connect(self.swap_tool_pane_widgets)

    def load_data(self, file, sep=",", encoding=None):
        """
        Wrapper for pandas function pd.read_csv. Uses that method to read data_frame from csv
        And then stores that data_frame in the class as self.data_frame
        Parameters
        ----------
        file : PATH
            DESCRIPTION.
        sep : String, optional
            DESCRIPTION. The default is ",".
        encoding : String, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        try:
            self.data_frame = pd.read_csv(file,sep = sep, encoding = encoding)
            self.current_data_frame = self.data_frame
            print("Successfully loaded data from: " + str(file))
        except:
            self.data_frame = None
            self.current_data_frame = None
            print("Unable to load data from: " + str(file))
        finally:
            self.update_gui_info() #Tell the embedded widgets the dataframe has changed
    
    def update_total_data(self):
        """
        Updates the display string with how much of the data remains after filtering
        """
        if self.data_frame is not None and self.current_data_frame is not None:
            total_rows = len(self.data_frame.index)
            subset_rows = len(self.current_data_frame.index)
            disp_str = "{0} of {1} rows match queries".format(str(subset_rows),str(total_rows))
            self.disp_label_number_rows.setText(disp_str)
        else:
            self.disp_label_number_rows.setText("No Data Available")
     
    def update_available_columns(self):
        """
        Call each tools widgets method for updating all applicable column dropdowns
        """
        for idx in range(self.display_stackedWidget_tools.count()):
            try:
                self.display_stackedWidget_tools.widget(idx).update_available_columns(self.current_data_frame)
            except:
                pass
    
    def swap_tool_pane_widgets(self):
        """
        Swaps out active widget in the stackedWidget
        """
        self.display_stackedWidget_tools.setCurrentIndex(self.display_cb_select_widget.currentIndex())
        
    def toggle_query_loc_btns(self):
        """
        Enables/Disables the undo/redo query buttons depending on past and current queries
        """
        self.display_btn_redo.setEnabled(self.current_query_location < len(self.queries))
        self.display_btn_undo.setEnabled(self.current_query_location > 0)
        
    def update_filter_history(self):
        texts = []
        for idx,query in enumerate(self.queries):
            if idx < self.current_query_location:
                texts.append(query["query_text"])
        for idx in range(self.display_stackedWidget_tools.count()):
            try:
                self.display_stackedWidget_tools.widget(idx).update_filter_history(texts)
            except:
                pass
    
    def get_current_data_frame(self):
        #This function returns the current data frame
        #The function can be passed as part of a query to prevent duplicate dataframe creations
        return self.current_data_frame
    
    def undo_query(self):
        """
        Undo works by starting from all data and reperforming the queries up to the last one done
        """
        self.current_data_frame = self.data_frame
        for idx, query in enumerate(self.queries): #Reapply all queries up until current one
            if idx + 1 >= self.current_query_location:
                break
            else:
                self.perform_query(query)
        self.current_query_location = self.current_query_location -1 #decrement the current query number
        self.update_gui_info()
        
        
    def redo_query(self):
        """
        Do the next stored query

        Returns
        -------
        None.

        """
        query = self.queries[self.current_query_location]
        self.current_query_location += 1
        self.perform_query(query,update_gui=True)
        
    def perform_query(self,query,update_gui=False, update_queries_list = False):
        """
        Handles all logic of the application for executing query and updating resultant info
        Parameters
        ----------
        query : Dict
            The dictionary representation of the functions/commands to execute.
        update_gui : BOOL, optional
            Whether to update the display after the query. The default is False.
        update_queries_list : BOOL, optional
            Whether to insert the query into the query list. The default is False.

        Returns
        -------
        None.

        """
        self.current_data_frame = self.evaluate_query(self.current_data_frame,query["query_func"], query["query_kwargs"])
        if update_queries_list:
            if self.current_query_location == len(self.queries):
                self.queries.append(query)
                self.current_query_location += 1
            elif self.current_query_location < len(self.queries):
                self.queries = self.queries[0:self.current_query_location]
                self.queries.append(query)
                self.current_query_location += 1
            else:
                print("Error encountered")
        if update_gui:
            self.update_gui_info()
        
    def evaluate_query(self, data_frame, query_func, query_kwargs):
        """

        Parameters
        ----------
        data_frame : pandas data frame
            The dataframe to perfrom the queries on.
        query_func : function handle
            The function that is being called.
        query_kwargs : dict
            dictionary representation of named arguments for query_func.

        Returns
        -------
        pandas data frame
            resultant filtered pandas dataframe

        """
        return data_frame[query_func(**query_kwargs)]
    
    def update_gui_info(self):
        self.update_total_data()
        self.update_available_columns()
        self.toggle_query_loc_btns()
        self.update_filter_history()
        
    def plot(self, plot_dict):
        """
        Handles calling plotting subfunctions

        Parameters
        ----------
        plot_dict : dict
            Dictionary of keyword arguments for plotting.

        Returns
        -------
        None.

        """
        self.graph.axes.clear()
        plot_type = plot_dict.get("mode","")
        if plot_type == "scatter":
            self.plot_scatter(plot_dict)
        elif plot_type =="bar":
            self.plot_bar(plot_dict)
       
    def plot_scatter(self,plot_dict):
        """
        Creates a scatter plot of 2 columns in the dataframe

        Parameters
        ----------
        plot_dict : dict
            Dictionary of keyword arguments for plotting.

        Returns
        -------
        None.

        """
        x = self.current_data_frame[plot_dict["data"]["x_data"]].tolist()
        y = self.current_data_frame[plot_dict["data"]["y_data"]].tolist()
        self.graph.axes.plot(x,y,marker='o', linestyle='none')
        self.graph.axes.set_xlabel(plot_dict["data"]["x_data"])
        self.graph.axes.set_ylabel(plot_dict["data"]["y_data"])
        self.graph.axes.set_title(plot_dict["options"]["title"])
        self.graph.draw()
            
    def plot_bar(self,plot_dict):
        """
        Creates a bar plot of 2 columns in the dataframe

        Parameters
        ----------
        plot_dict : dict
            Dictionary of keyword arguments for plotting.

        Returns
        -------
        None.

        """
        family_text = plot_dict["data"]["families"]
        families = []
        if family_text != "None":
            family_attr = self.current_data_frame[family_text].tolist()
            family_sets = set(family_attr) #Get all unique values
            families=[val for val in family_sets if not pd.isnull(val)] #Remove Nans
            if len(families) != len(family_sets):
                #Add a representation of missing data
                families.append("NANDATA")
        count_text = plot_dict["data"]["count"]
        count_set = set(self.current_data_frame[count_text].tolist())
        count_categories = [val for val in count_set if not pd.isnull(val)] #Remove Nans
        if len(count_categories) != len(count_set):
            #Add a representation of missing data
            count_categories.append("NANDATA") 
        if not families:#If the none option was passed, we want all the data
            families=["All Data"]
        plot_data_frame = self._get_bar_subtotals_df(count_text, count_categories, families, family_text, percent=plot_dict["options"]["percentage"])  
        labels=plot_data_frame["Family"].tolist()
        num_bars = len(count_categories)
        width=1/(num_bars+2)
        x_vals = np.arange(len(labels))
        offsets =self._get_bar_offsets(x_vals,width, num_bars,plot_dict["options"]["stacked"])
        bottoms = [0] * len(labels) # Initial bottom state should all be at 0
        for offset,current_category in enumerate(count_categories):
            values = plot_data_frame[current_category].tolist()
            bars = self.graph.axes.bar(offsets[offset],values,width,bottom=bottoms,label=current_category)
            if plot_dict["options"]["stacked"]:
                bottoms = list(map(add,bottoms,values)) #Set new bottom values
        self.graph.axes.set_ylabel(count_text + " count")
        if family_text != 'None':
            self.graph.axes.set_xlabel(family_text + " value groupings")
            self.graph.axes.set_title(count_text + " counts by " + family_text)
        else:
            self.graph.axes.set_title(count_text + " counts")
        self.graph.axes.set_xticks(x_vals)
        self.graph.axes.set_xticklabels(labels)
        self.graph.axes.legend()
        self.graph.draw()
    
    def _get_bar_offsets(self,x_vals,width,num_bars,stacked=False):
        """
        Gets the offset arrays for x locations of bars in bar chart

        Parameters
        ----------
        x_vals : np array
            the center x values for each grouping of bars.
        width : float
            the width of each bar.
        num_bars : int
            number of bars per family.
        stacked : boolean, optional
            If the bars are stacked vertically. The default is False.

        Returns
        -------
        offsets : np array
            the calculated offsets per bar.
        """
        offsets=[]
        if stacked:
            for i in range(0,num_bars): #If all bars in a family are stacked, they share an x value
                offsets.append(x_vals)
        elif num_bars%2 == 0: #For even number of bars, have equal number above/below x
            max_level = int(num_bars/2)
            for i in range(max_level,0,-1):
                offsets.append(x_vals-i*width +width/2)
            for i in range(0,max_level):
                offsets.append(x_vals+i*width+width/2)
        else:
            max_level = int(num_bars//2)  #for odd number of bars, we straddle the x value then even numbers on either side
            for i in range(max_level,0,-1):
                offsets.append(x_vals-i*width)
            offsets.append(x_vals)
            for i in range(0,max_level):
                offsets.append(x_vals+(i+1)*width)
        return offsets
        
    def _get_bar_subtotals_df(self,count_column,count_categories,families, family_column=None,percent=False):
        """
        Calculates the subtotals of each grouping for the bar chart

        Parameters
        ----------
        count_column : String
            Key of the column to count from.
        count_categories : list
            The values of the column we are counting for.
        families : String
            The family values we are grouping by.
        family_column : String, optional
            The key of the column that represents families. The default is None.
        percent : boolean, optional
            If we are normalizing the counts to percents of family. The default is False.

        Returns
        -------
        plot_data_frame : pandas dataframe
            The dataframe representing the counts for each bar.

        """
        df_columns = ["Family"] + count_categories
        plot_data_frame = pd.DataFrame(columns=df_columns)
        for family in families:
            family_dict={"Family":family}
            if percent and family != "All Data":
                total = self._get_count_one_condition(self.current_data_frame,family_column,family)/100
            elif percent and family == "All Data":
                total=len(self.current_data_frame)/100
            else:
                total= 1;
            for category in count_categories:
                if family == "All Data":
                    local_count = self._get_count_one_condition(self.current_data_frame,count_column,category)/total
                else:
                    local_count = self._get_count(self.current_data_frame,count_column,category,family_column,family)/total
                family_dict[category]=local_count
            plot_data_frame=plot_data_frame.append(family_dict,ignore_index=True)
        return plot_data_frame
    
    def _get_count_one_condition(self, df, col1, col1val):
        """

        Parameters
        ----------
        df : pandas dataframe
            The dataframe to count from.
        col1 : String
            The column key to count from.
        col1val : String
            The column value to count for.

        Returns
        -------
        int
            the count of matching items.
        """
        
        if col1val == "NANDATA":
            return len(df[(pd.isnull(df[col1]))])
        else:
            return len(df[(df[col1] == col1val)])
        
    def _get_count(self, df, col1, col1val,col2,col2val):
        """

        Parameters
        ----------
        df : pandas dataframe
            The dataframe to count from.
        col1 : String
            The key of the first column to count from.
        col1val : String
            The value in the first column to look for.
        col2 : String
            The key of the second column to count from.
        col2val : String
            The value in the second column to look for.

        Returns
        -------
        int
            The number of items that match the requested search.

        """
        if col1val == "NANDATA" and col2val == "NANDATA":
            return len(df[(pd.isnull(df[col1])) & (pd.isnull(df[col2]))])
        elif col1val == "NANDATA":
            return len(df[(pd.isnull(df[col1])) & (df[col2] ==col2val)])
        elif col2val == "NANDATA":
            return len(df[(df[col1] == col1val) & (pd.isnull(df[col2]))])
        else:
            return len(df[(df[col1] == col1val) & (df[col2] ==col2val)])
        
    def save_plot(self):
        filename, _discard = QFileDialog.getSaveFileName(self, 'Choose Save File',filter='*.png')
        if filename:
            try:
                self.graph.figure.savefig(filename)
            except:
                print("Unable to save file")
        
class FileOpenCSVWidget(QWidget,FileOpenCSVWidget.Ui_file_open_csv_widget):
    """
    Class for the popup widget to allow users to search for and load their csv file
    """
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.filename = ''
        self.make_connections()
        self.file_btn_loadcsv.setEnabled(False)
    
    def make_connections(self):
        self.file_btn_loadcsv.clicked.connect(self.load_btn_action)
        self.file_btn_open.clicked.connect(self.pick_csv)
        
    def pick_csv(self):
        """
        Opens a dialog box that lets users search for a file and specify any encoding info

        Returns
        -------
        None.

        """
        #Qfiledialog returns a tuple
        filename, _discard = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser("~"),"CSV File (*.csv)")
        self.filename = filename
        self.file_txt_filename = str(filename)
        #Enable the button only if a file was specified 
        self.file_btn_loadcsv.setEnabled(filename is not None and filename != '')

    def load_btn_action(self):
        """
        Tell the main widget the paramaters to try to load

        Returns
        -------
        None.

        """
        encoding = self.file_cb_encoding.currentText()
        sep = self.file_txt_sep.text()
        if not sep:
            sep = ","
        self.parent.load_data(self.filename, sep=sep, encoding=encoding)
        self.hide()

class MplCanvas(FigureCanvasQTAgg):
    """
    Class for object oriented approach to matplotlib
    The basics of this class are taken from https://www.learnpyqt.com/courses/graphics-plotting/plotting-matplotlib/
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)     
        

