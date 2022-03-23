# Pyside6 MainWindow view
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)
# from __feature__ import snake_case, true_property
# ==> can not use features with files generated from pyside6-uic (Ui_MainWindow)
from View.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @Slot(bool)
    def on_actionQuitter_triggered(self, checked=False):
        """Quit application when QAction from MenuActions Quit has been clicked"""
        quit()

    @Slot(bool)
    def on_actionTest_de_connection_triggered(self, checked=False):
        """Test USB connection to Arduino Solar Tracker"""
        self.statusbar.showMessage("Test connection USB with Arduino Solar Tracker...")

