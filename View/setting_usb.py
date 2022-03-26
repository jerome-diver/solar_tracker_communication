"""Dialog USB setting to config USB connection with Solar tracker hardware"""

from PySide6.QtWidgets import QDialog
from View.ui_setting_usb import Ui_Dialog_USB_setting


class DialogSettingUSB(QDialog, Ui_Dialog_USB_setting):
    "You have to provide the controller when you 'instanciate' this object"

    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.ctrl = controller
        self.ctrl.communication.config_view = self
        self.buttonBox.clicked.connect(self.on_clicked_buttonBox)
        self.button_test_connection.clicked.connect(self.on_button_test_connection_clicked)
        self.button_test_connection.clicked.connect(self.ctrl.views_actions.actionTest_de_connection_triggered)

    def on_clicked_buttonBox(self, button):
        print("ok from USB setting")
        print(button)

    def on_button_test_connection_clicked(self):
        print("clicked test")
