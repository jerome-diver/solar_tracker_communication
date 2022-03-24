# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_usbluVGnO.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
import sys
sys.path.insert(0, "./images")
import resources_rc

class Ui_Dialog_USB_setting(object):
    def setupUi(self, Dialog_USB_setting):
        if not Dialog_USB_setting.objectName():
            Dialog_USB_setting.setObjectName(u"Dialog_USB_setting")
        Dialog_USB_setting.resize(320, 240)
        self.gridLayout = QGridLayout(Dialog_USB_setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_icon = QLabel(Dialog_USB_setting)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setPixmap(QPixmap(u":/icons/USB_plug.png"))

        self.gridLayout.addWidget(self.label_icon, 0, 0, 2, 1)

        self.label_port = QLabel(Dialog_USB_setting)
        self.label_port.setObjectName(u"label_port")

        self.gridLayout.addWidget(self.label_port, 0, 1, 1, 1)

        self.button_test_connection = QPushButton(Dialog_USB_setting)
        self.button_test_connection.setObjectName(u"button_test_connection")
        self.button_test_connection.setMinimumSize(QSize(0, 64))
        icon = QIcon()
        icon.addFile(u":/icons/arduino_icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_test_connection.setIcon(icon)
        self.button_test_connection.setIconSize(QSize(48, 48))
        self.button_test_connection.setFlat(False)

        self.gridLayout.addWidget(self.button_test_connection, 2, 0, 1, 4)

        self.buttonBox = QDialogButtonBox(Dialog_USB_setting)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)

        self.label_baudrate = QLabel(Dialog_USB_setting)
        self.label_baudrate.setObjectName(u"label_baudrate")

        self.gridLayout.addWidget(self.label_baudrate, 1, 1, 1, 1)

        self.comboBox_baudrate = QComboBox(Dialog_USB_setting)
        self.comboBox_baudrate.setObjectName(u"comboBox_baudrate")

        self.gridLayout.addWidget(self.comboBox_baudrate, 1, 2, 1, 2)

        self.comboBox_port = QComboBox(Dialog_USB_setting)
        self.comboBox_port.setObjectName(u"comboBox_port")

        self.gridLayout.addWidget(self.comboBox_port, 0, 2, 1, 2)


        self.retranslateUi(Dialog_USB_setting)
        self.buttonBox.accepted.connect(Dialog_USB_setting.accept)
        self.buttonBox.rejected.connect(Dialog_USB_setting.reject)

        self.button_test_connection.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog_USB_setting)
    # setupUi

    def retranslateUi(self, Dialog_USB_setting):
        Dialog_USB_setting.setWindowTitle(QCoreApplication.translate("Dialog_USB_setting", u"Configuration USB", None))
        self.label_icon.setText("")
        self.label_port.setText(QCoreApplication.translate("Dialog_USB_setting", u"port", None))
        self.button_test_connection.setText(QCoreApplication.translate("Dialog_USB_setting", u"Test connection", None))
        self.label_baudrate.setText(QCoreApplication.translate("Dialog_USB_setting", u"Vitesse", None))
    # retranslateUi

