# Pyside6 MainWindow view
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTime
# from __feature__ import snake_case, true_property
# ==> can not use features with files generated from pyside6-uic (Ui_MainWindow)
from View.ui_mainwindow import Ui_MainWindow
from Controller.control import Control


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_ctrl = Control()
        self.menu_ctrl.menu_actions = self
        self.timeEdit_locale.setTime(QTime.currentTime())
        self.timeEdit_locale.setReadOnly(True)
