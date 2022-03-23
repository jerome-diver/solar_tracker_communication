# Pyside6 MainWindow view
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)
# from __feature__ import snake_case, true_property
# ==> can not use features with files generated from pyside6-uic (Ui_MainWindow)
from View.ui_mainwindow import Ui_MainWindow
from Controller.menu_actions import MenuActions


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_actions = MenuActions(self)


