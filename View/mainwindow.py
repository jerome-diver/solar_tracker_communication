# Pyside6 MainWindow view

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)
# from __feature__ import snake_case, true_property
# ==> can not use features with files generated from pyside6-uic (Ui_MainWindow)
from View.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
