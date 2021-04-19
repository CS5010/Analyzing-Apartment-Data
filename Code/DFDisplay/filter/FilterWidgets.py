# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:29:28 2020

@author: Dave
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ui.FilterWidget import Ui_FilterWidget
from ui.FilterQueryWidget import Ui_FilterQueryWidget
from ui.FilterHistoryWidget import Ui_FilterHistoryWidget

class FilterWidget(QWidget,Ui_FilterWidget):
    """
    Top level Widget for handling the various widgets associated with filtering the dataframe
    """
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.filter_widget_query = FilterQueryWidget()
        self.add_sub_widget(self.filter_widget_query,"Query")
        self.add_sub_widget(FilterHistoryWidget(),"History")
        self.parent = parent
        self.make_connections()
        

    def make_connections(self):
        """
        Connect actions to functions
        """
        self.filter_btn_submit.clicked.connect(self.send_filter_query)
        self.filter_actions_cb.currentIndexChanged.connect(self.swap_filter_type_widgets)
    
    def swap_filter_type_widgets(self):
        self.filter_stacked_widget.setCurrentIndex(self.filter_actions_cb.currentIndex())
        self.filter_btn_submit.setEnabled(self.filter_stacked_widget.currentWidget().enable_filter)
    
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
        self.filter_stacked_widget.addWidget(widget)
        self.filter_actions_cb.addItems([label])
    
    
    def update_available_columns(self,data_frame):
        """
        Pass the data_frame to embedded widgets so they can update their respective dropdown boxes
        """
        num_widgets = self.filter_stacked_widget.count()
        for idx in range(num_widgets):
            widget = self.filter_stacked_widget.widget(idx)
            widget.update_available_columns(data_frame)
    
    def update_filter_history(self, texts):
        num_widgets = self.filter_stacked_widget.count()
        for idx in range(num_widgets):
            widget = self.filter_stacked_widget.widget(idx)
            try:
                widget.update_filter_history(texts)
            except:
                pass
            
    def send_filter_query(self):
        """
        Build the filter_query dictionary and pass to dfDisplay to be processed
        """
        query=self.filter_widget_query.build_local_query(self.parent.get_current_data_frame)
        self.parent.perform_query(query=query, update_gui=True, update_queries_list=True)
        
class FilterQueryWidget(QWidget,Ui_FilterQueryWidget):
    """
    Widget for getting user input about how to filter the dataframe and packages it
    Into a complex dictionary that can be used to filter without storing more dataframes
    in memory.
    """
    def __init__(self,):
        super().__init__()
        self.setupUi(self)
        self.enable_filter = True
    
    def update_available_columns(self,data_frame):
        """
        Update the comboboxes with available column choices
        """
        col_list = data_frame.columns.to_list()
        col_list.sort()
        self.cb_columns.clear()
        self.cb_columns.addItems(col_list)
    
    def build_local_query(self, data_frame=None):
        """
        Build a dictionary representation of the user input fields.
        
        Parameters
        ----------
        data_frame : Pandas dataframe, optional
            A dataframe to apply the filter to. The default is None.

        Returns
        -------
        query_dict : dict
            The dictionary of nested function calls and keyword arguments
            That represents a filter action.

        """
        value = self.txt_target_val.text()
        try:
            value = float(value) #If numeric, make it a float
        except:
            value = self.txt_target_val.text()
        query_kwargs = {
            "data_frame":data_frame,
            "column":self.cb_columns.currentText(),
            "operation":self.cb_operations.currentText(),
            "value":value
        }
        query_func = self.filter_query
        query_text = query_kwargs["column"] + " " + query_kwargs["operation"] +" " + str(query_kwargs["value"])
        query_dict = {
            "query_func":query_func,
            "query_kwargs":query_kwargs,
            "query_text": query_text
            }
        
        return query_dict
        """
        Sample
        #bedrooms = 5 & bathrooms =2
        q1={"data_frame":data_frame,"column":"bedrooms","operation":"=","value":5}
        q2={"data_frame":data_frame,"column":"bathrooms","operation":"=","value":2}
        q3={"data_frame":data_frame,
         "query1_func": self.filter_query,
         "query1_kwargs": q1,
         "query2_func": self.filter_query,
         "query2_kwargs": q2,
         }
        """
        
        
    def filter_query(self, data_frame, column, operation, value):
        """
        Execute a filter_query and return the resultant dataframe
        Data_frame may be a function to return a data_frame
        this is done to prevent duplication of data frames in memory
        """
        if type(data_frame).__name__ == 'method':
            output = data_frame()
        else:
            ouput = data_frame
        if operation == "=":
            output = output[column] == value
        elif operation == "<=":
            output = output[column] <= value
        elif operation == "<":
            output = output[column] < value
        elif operation == ">=":
            output = output[column] >= value
        elif operation == ">":
            output = output[column] > value
        return output
    
    def filter_and_query(self, data_frame, query1_func,query1_kwargs, query2_kwargs, query2_func):
        """
        This method is currently not used. It would allow for an "AND" operation to be done
        To combine two filters
        """
        return (query1_func(**query1_kwargs)) & (query2_func(**query2_kwargs))

class FilterHistoryWidget(QWidget,Ui_FilterHistoryWidget):
    """
    Class used for displaying the filter history
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.enable_filter = False
        self.filter_history_text = []
    
    def update_filter_history(self, text):
        self.filter_history_text = text
        self.build_filter_history_text()
        
    def build_filter_history_text(self):
        output = ""
        for idx,text in enumerate(self.filter_history_text):
            output += str(idx+1) + ".\t" + text +"\n"
        self.filt_history_label_history.setText(output)
    
    def update_available_columns(self, data_frame):
        pass
            
    