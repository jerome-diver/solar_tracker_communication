# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_connectionixPBFz.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)
import sys
sys.path.insert(0, "./images")
import resources_rc

class Ui_Dialog_test_connection(object):
    def setupUi(self, Dialog_test_connection):
        if not Dialog_test_connection.objectName():
            Dialog_test_connection.setObjectName(u"Dialog_test_connection")
        Dialog_test_connection.resize(390, 349)
        self.gridLayout = QGridLayout(Dialog_test_connection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_icon = QLabel(Dialog_test_connection)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setPixmap(QPixmap(u":/icons/arduino_icon.png"))

        self.gridLayout.addWidget(self.label_icon, 0, 0, 1, 1)

        self.label_arduino = QLabel(Dialog_test_connection)
        self.label_arduino.setObjectName(u"label_arduino")
        self.label_arduino.setMaximumSize(QSize(128, 128))
        self.label_arduino.setPixmap(QPixmap(u":/icons/Arduino-Nano-hardware v3_0 photo.png"))
        self.label_arduino.setScaledContents(True)

        self.gridLayout.addWidget(self.label_arduino, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog_test_connection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 0, 4, 1, 1)

        self.text = QTextEdit(Dialog_test_connection)
        self.text.setObjectName(u"text")
        self.text.setReadOnly(True)

        self.gridLayout.addWidget(self.text, 2, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.button_test = QPushButton(Dialog_test_connection)
        self.button_test.setObjectName(u"button_test")
        font = QFont()
        font.setFamilies([u"Corbel"])
        font.setPointSize(16)
        font.setBold(True)
        font.setKerning(False)
        self.button_test.setFont(font)
        self.button_test.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.button_test, 1, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.retranslateUi(Dialog_test_connection)
        self.buttonBox.accepted.connect(Dialog_test_connection.accept)
        self.buttonBox.rejected.connect(Dialog_test_connection.reject)

        QMetaObject.connectSlotsByName(Dialog_test_connection)
    # setupUi

    def retranslateUi(self, Dialog_test_connection):
        Dialog_test_connection.setWindowTitle(QCoreApplication.translate("Dialog_test_connection", u"Test de connection", None))
        self.label_icon.setText("")
        self.label_arduino.setText("")
        self.button_test.setText(QCoreApplication.translate("Dialog_test_connection", u"Test", None))
    # retranslateUi

