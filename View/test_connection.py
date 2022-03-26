"""Dialog Test connection window to test the connection with the Solar Tracker hardware"""

from PySide6.QtWidgets import QDialog
from View.ui_test_connection import Ui_Dialog_test_connection


class DialogTestConnection(QDialog, Ui_Dialog_test_connection):
    """You have to provide the controller when you 'instanciate' this object"""


    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.button_test.set_disabled(True)
        self.ctrl = controller
        self.ctrl.communication.test_view = self
        self.buttonBox.clicked.connect(self.ctrl.views_actions.on_clicked_buttonBox)
        self.button_test.clicked.connect(self.ctrl.communication.test)
