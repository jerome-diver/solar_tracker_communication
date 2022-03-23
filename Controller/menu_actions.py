from PySide6.QtCore import Slot


class MenuActions:
    def __init__(self, ui):
        print("OK")
        self.ui = ui
        self.ui.actionQuitter.triggered.connect(self.actionQuitter_triggered)
        self.ui.actionTest_de_connection.triggered.connect(self.actionTest_de_connection_triggered)

    @Slot(bool)
    def actionQuitter_triggered(self, checked=False):
        """Quit application when QAction from MenuActions Quit has been clicked"""
        quit()

    @Slot(bool)
    def actionTest_de_connection_triggered(self, checked=False):
        """Test USB connection to Arduino Solar Tracker"""
        self.ui.statusbar.showMessage("Test connection USB with Arduino Solar Tracker...")
