# Communicate with Arduino Nano project Solar Tracker
# To be able to set date and time to RTC DS3232
# To be able to read wake up sun time and sleeping time of the day and coordinates for each from HMC5983

from PySide6.QtWidgets import QApplication

from View.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()
