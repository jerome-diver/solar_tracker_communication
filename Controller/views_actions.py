from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QObject, Signal, Slot


class ViewsActions:
    """Views actions controller"""

    config_usb_change = Signal((str, str), (str, int))    # when a setting change, this signal emit what's the change is about

    def __init__(self, ui):
        self.ui = ui
        self.ui.actionQuitter.triggered.connect(self.actionQuitter_triggered)
        self.ui.actionTest_de_connection.triggered.connect(self.actionTest_de_connection_triggered)
        self.ui.action_USB_setting.triggered.connect(self.actionUSB_setting_triggered)

    @Slot(bool)
    def actionQuitter_triggered(self, checked=False):
        """Quit application when QAction from ViewsActions Quit has been clicked"""
        quit()

    @Slot(bool)
    def actionTest_de_connection_triggered(self, checked=False):
        """Test USB connection to Arduino Solar Tracker"""
        self.ui.statusbar.showMessage("Test connection USB with Arduino Solar Tracker...")
        self.ui.dialog_test_connection.exec()

    @Slot(bool)
    def actionUSB_setting_triggered(self, checked=False):
        """Open Dialog USB setting"""
        self.ui.dialog_usb_setting.exec()

    @Slot(QPushButton)
    def on_clicked_buttonBox(self, button):
        """actions from buttons box [OK|CANCEL] view"""
        if (button.text() == "OK"):
            print("ok from connection test view")
        else:
            print("Cancel from connection test view")

    @Slot(str)
    def on_port_changed(self, port):
        self.config_usb_change[str, str].emit("port", port)
