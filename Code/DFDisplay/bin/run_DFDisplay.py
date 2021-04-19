# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from pathlib import Path

#Tell the app that all import paths will be relative to this top level folder
module_path = Path(__file__).parents[1]
if str(module_path) not in sys.path:
    sys.path.insert(1, str(module_path))
else:
    sys.path.remove(str(module_path))
    sys.path.insert(1, str(module_path))
    
from DFMain.DFMain import DFMainWindow
def main():

   app = QApplication(sys.argv)
   window = DFMainWindow()
   window.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()