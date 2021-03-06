# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowabPVnD.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTimeEdit,
    QVBoxLayout, QWidget)
import sys
sys.path.insert(0, "./images")
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 666)
        icon = QIcon()
        icon.addFile(u":/icons/solar_track.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(32, 32))
        self.action_USB_setting = QAction(MainWindow)
        self.action_USB_setting.setObjectName(u"action_USB_setting")
        self.action_Date_et_heure = QAction(MainWindow)
        self.action_Date_et_heure.setObjectName(u"action_Date_et_heure")
        self.action_Unit = QAction(MainWindow)
        self.action_Unit.setObjectName(u"action_Unit")
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionTest_de_connection = QAction(MainWindow)
        self.actionTest_de_connection.setObjectName(u"actionTest_de_connection")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(32, 32))
        self.date_time = QWidget()
        self.date_time.setObjectName(u"date_time")
        palette = QPalette()
        self.date_time.setPalette(palette)
        self.date_time.setToolTipDuration(5)
        self.date_time.setAutoFillBackground(False)
        self.date_time.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.date_time)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.date_time_widget = QWidget(self.date_time)
        self.date_time_widget.setObjectName(u"date_time_widget")
        self.date_time_widget.setMaximumSize(QSize(16777215, 350))
        self.gridLayout_2 = QGridLayout(self.date_time_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.timeEdit_locale = QTimeEdit(self.date_time_widget)
        self.timeEdit_locale.setObjectName(u"timeEdit_locale")

        self.gridLayout_2.addWidget(self.timeEdit_locale, 2, 2, 1, 1)

        self.label_locale = QLabel(self.date_time_widget)
        self.label_locale.setObjectName(u"label_locale")
        self.label_locale.setMinimumSize(QSize(0, 64))
        self.label_locale.setMaximumSize(QSize(16777215, 50))
        self.label_locale.setPixmap(QPixmap(u":/icons/local_world.png"))
        self.label_locale.setScaledContents(False)
        self.label_locale.setAlignment(Qt.AlignCenter)
        self.label_locale.setMargin(5)

        self.gridLayout_2.addWidget(self.label_locale, 0, 2, 1, 1)

        self.label_solar_tracker = QLabel(self.date_time_widget)
        self.label_solar_tracker.setObjectName(u"label_solar_tracker")
        self.label_solar_tracker.setMinimumSize(QSize(0, 64))
        self.label_solar_tracker.setMaximumSize(QSize(16777215, 50))
        self.label_solar_tracker.setPixmap(QPixmap(u":/icons/solar_track_1.png"))
        self.label_solar_tracker.setScaledContents(False)
        self.label_solar_tracker.setAlignment(Qt.AlignCenter)
        self.label_solar_tracker.setMargin(5)

        self.gridLayout_2.addWidget(self.label_solar_tracker, 0, 3, 1, 1)

        self.label_time = QLabel(self.date_time_widget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMaximumSize(QSize(100, 16777215))
        self.label_time.setPixmap(QPixmap(u":/icons/clock_time.png"))
        self.label_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_time, 2, 1, 1, 1)

        self.timeEdit_solar_tracker = QTimeEdit(self.date_time_widget)
        self.timeEdit_solar_tracker.setObjectName(u"timeEdit_solar_tracker")

        self.gridLayout_2.addWidget(self.timeEdit_solar_tracker, 2, 3, 1, 1)

        self.label_date = QLabel(self.date_time_widget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMaximumSize(QSize(100, 16777215))
        self.label_date.setPixmap(QPixmap(u":/icons/calendar.png"))
        self.label_date.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_date, 1, 1, 1, 1)

        self.read_data_rtc_action = QPushButton(self.date_time_widget)
        self.read_data_rtc_action.setObjectName(u"read_data_rtc_action")
        self.read_data_rtc_action.setStyleSheet(u"color: \"green\"")

        self.gridLayout_2.addWidget(self.read_data_rtc_action, 3, 3, 1, 1)

        self.write_data_rtc_action = QPushButton(self.date_time_widget)
        self.write_data_rtc_action.setObjectName(u"write_data_rtc_action")
        self.write_data_rtc_action.setStyleSheet(u"color: 'red';")

        self.gridLayout_2.addWidget(self.write_data_rtc_action, 3, 2, 1, 1)

        self.calendar_locale = QCalendarWidget(self.date_time_widget)
        self.calendar_locale.setObjectName(u"calendar_locale")

        self.gridLayout_2.addWidget(self.calendar_locale, 1, 2, 1, 1)

        self.calendar_solar_tracker = QCalendarWidget(self.date_time_widget)
        self.calendar_solar_tracker.setObjectName(u"calendar_solar_tracker")

        self.gridLayout_2.addWidget(self.calendar_solar_tracker, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.date_time_widget)

        icon1 = QIcon()
        icon1.addFile(u":/icons/calendrier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.date_time, icon1, "")
        self.start = QWidget()
        self.start.setObjectName(u"start")
        self.verticalLayout_3 = QVBoxLayout(self.start)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.start_of_day = QGroupBox(self.start)
        self.start_of_day.setObjectName(u"start_of_day")
        self.gridLayout = QGridLayout(self.start_of_day)
        self.gridLayout.setObjectName(u"gridLayout")
        self.calendar_start = QCalendarWidget(self.start_of_day)
        self.calendar_start.setObjectName(u"calendar_start")
        self.calendar_start.setMaximumSize(QSize(16777215, 200))

        self.gridLayout.addWidget(self.calendar_start, 1, 1, 1, 1)

        self.label_date_start = QLabel(self.start_of_day)
        self.label_date_start.setObjectName(u"label_date_start")
        self.label_date_start.setPixmap(QPixmap(u":/icons/calendar.png"))
        self.label_date_start.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_date_start, 1, 0, 1, 1)

        self.read_data_start_action = QPushButton(self.start_of_day)
        self.read_data_start_action.setObjectName(u"read_data_start_action")

        self.gridLayout.addWidget(self.read_data_start_action, 0, 0, 1, 5)

        self.label_time_start = QLabel(self.start_of_day)
        self.label_time_start.setObjectName(u"label_time_start")
        self.label_time_start.setPixmap(QPixmap(u":/icons/clock_time.png"))
        self.label_time_start.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_time_start, 1, 2, 1, 1)

        self.groupBox_magneto_start = QGroupBox(self.start_of_day)
        self.groupBox_magneto_start.setObjectName(u"groupBox_magneto_start")
        self.gridLayout_3 = QGridLayout(self.groupBox_magneto_start)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_head_start = QLineEdit(self.groupBox_magneto_start)
        self.lineEdit_head_start.setObjectName(u"lineEdit_head_start")

        self.gridLayout_3.addWidget(self.lineEdit_head_start, 3, 2, 1, 1)

        self.lineEdit_Y_start = QLineEdit(self.groupBox_magneto_start)
        self.lineEdit_Y_start.setObjectName(u"lineEdit_Y_start")

        self.gridLayout_3.addWidget(self.lineEdit_Y_start, 1, 2, 1, 1)

        self.lineEdit_Z_start = QLineEdit(self.groupBox_magneto_start)
        self.lineEdit_Z_start.setObjectName(u"lineEdit_Z_start")

        self.gridLayout_3.addWidget(self.lineEdit_Z_start, 2, 2, 1, 1)

        self.lineEdit_X_start = QLineEdit(self.groupBox_magneto_start)
        self.lineEdit_X_start.setObjectName(u"lineEdit_X_start")

        self.gridLayout_3.addWidget(self.lineEdit_X_start, 0, 2, 1, 1)

        self.label_Y_start = QLabel(self.groupBox_magneto_start)
        self.label_Y_start.setObjectName(u"label_Y_start")
        self.label_Y_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_Y_start, 1, 1, 1, 1)

        self.label_X_start = QLabel(self.groupBox_magneto_start)
        self.label_X_start.setObjectName(u"label_X_start")
        self.label_X_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_X_start, 0, 1, 1, 1)

        self.label_Z_start = QLabel(self.groupBox_magneto_start)
        self.label_Z_start.setObjectName(u"label_Z_start")
        self.label_Z_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_Z_start, 2, 1, 1, 1)

        self.label_magnetometer_start = QLabel(self.groupBox_magneto_start)
        self.label_magnetometer_start.setObjectName(u"label_magnetometer_start")
        self.label_magnetometer_start.setPixmap(QPixmap(u":/icons/magnetometer 3 axes.png"))

        self.gridLayout_3.addWidget(self.label_magnetometer_start, 0, 0, 3, 1)

        self.label_head_start = QLabel(self.groupBox_magneto_start)
        self.label_head_start.setObjectName(u"label_head_start")
        self.label_head_start.setPixmap(QPixmap(u":/icons/compass.png"))
        self.label_head_start.setScaledContents(False)

        self.gridLayout_3.addWidget(self.label_head_start, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_magneto_start, 4, 2, 1, 3)

        self.groupBox_servo_start = QGroupBox(self.start_of_day)
        self.groupBox_servo_start.setObjectName(u"groupBox_servo_start")
        self.horizontalLayout = QHBoxLayout(self.groupBox_servo_start)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_servo_start = QLabel(self.groupBox_servo_start)
        self.label_servo_start.setObjectName(u"label_servo_start")
        self.label_servo_start.setPixmap(QPixmap(u":/icons/servo 1.png"))

        self.horizontalLayout.addWidget(self.label_servo_start)

        self.lineEdit_servo_start = QLineEdit(self.groupBox_servo_start)
        self.lineEdit_servo_start.setObjectName(u"lineEdit_servo_start")
        self.lineEdit_servo_start.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lineEdit_servo_start)


        self.gridLayout.addWidget(self.groupBox_servo_start, 4, 0, 1, 2)

        self.timeEdit_time_start = QTimeEdit(self.start_of_day)
        self.timeEdit_time_start.setObjectName(u"timeEdit_time_start")

        self.gridLayout.addWidget(self.timeEdit_time_start, 1, 3, 1, 2)


        self.verticalLayout_3.addWidget(self.start_of_day)

        icon2 = QIcon()
        icon2.addFile(u":/icons/sunrise 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.start, icon2, "")
        self.end = QWidget()
        self.end.setObjectName(u"end")
        self.verticalLayout_4 = QVBoxLayout(self.end)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.end_of_day = QGroupBox(self.end)
        self.end_of_day.setObjectName(u"end_of_day")
        self.gridLayout_4 = QGridLayout(self.end_of_day)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.read_data_end_action = QPushButton(self.end_of_day)
        self.read_data_end_action.setObjectName(u"read_data_end_action")

        self.gridLayout_4.addWidget(self.read_data_end_action, 0, 0, 1, 5)

        self.label_date_end = QLabel(self.end_of_day)
        self.label_date_end.setObjectName(u"label_date_end")
        self.label_date_end.setPixmap(QPixmap(u":/icons/calendar.png"))
        self.label_date_end.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_date_end, 1, 0, 1, 1)

        self.calendar_end = QCalendarWidget(self.end_of_day)
        self.calendar_end.setObjectName(u"calendar_end")
        self.calendar_end.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_4.addWidget(self.calendar_end, 1, 1, 1, 1)

        self.label_time_end = QLabel(self.end_of_day)
        self.label_time_end.setObjectName(u"label_time_end")
        self.label_time_end.setPixmap(QPixmap(u":/icons/clock_time.png"))
        self.label_time_end.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_time_end, 1, 2, 1, 1)

        self.servo_end = QGroupBox(self.end_of_day)
        self.servo_end.setObjectName(u"servo_end")
        self.horizontalLayout_2 = QHBoxLayout(self.servo_end)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_servo_end = QLabel(self.servo_end)
        self.label_servo_end.setObjectName(u"label_servo_end")
        self.label_servo_end.setPixmap(QPixmap(u":/icons/servo 1.png"))

        self.horizontalLayout_2.addWidget(self.label_servo_end)

        self.lineEdit_servo_end = QLineEdit(self.servo_end)
        self.lineEdit_servo_end.setObjectName(u"lineEdit_servo_end")

        self.horizontalLayout_2.addWidget(self.lineEdit_servo_end)


        self.gridLayout_4.addWidget(self.servo_end, 2, 0, 1, 2)

        self.groupBox_megneto_end = QGroupBox(self.end_of_day)
        self.groupBox_megneto_end.setObjectName(u"groupBox_megneto_end")
        self.gridLayout_5 = QGridLayout(self.groupBox_megneto_end)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_Z_end = QLineEdit(self.groupBox_megneto_end)
        self.lineEdit_Z_end.setObjectName(u"lineEdit_Z_end")

        self.gridLayout_5.addWidget(self.lineEdit_Z_end, 2, 2, 1, 1)

        self.label_Y_end = QLabel(self.groupBox_megneto_end)
        self.label_Y_end.setObjectName(u"label_Y_end")
        self.label_Y_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_Y_end, 1, 1, 1, 1)

        self.lineEdit_X_end = QLineEdit(self.groupBox_megneto_end)
        self.lineEdit_X_end.setObjectName(u"lineEdit_X_end")

        self.gridLayout_5.addWidget(self.lineEdit_X_end, 0, 2, 1, 1)

        self.lineEdit_Y_end = QLineEdit(self.groupBox_megneto_end)
        self.lineEdit_Y_end.setObjectName(u"lineEdit_Y_end")

        self.gridLayout_5.addWidget(self.lineEdit_Y_end, 1, 2, 1, 1)

        self.label_X_end = QLabel(self.groupBox_megneto_end)
        self.label_X_end.setObjectName(u"label_X_end")
        self.label_X_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_X_end, 0, 1, 1, 1)

        self.label_Z_end = QLabel(self.groupBox_megneto_end)
        self.label_Z_end.setObjectName(u"label_Z_end")
        self.label_Z_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_Z_end, 2, 1, 1, 1)

        self.lineEdit_head_end = QLineEdit(self.groupBox_megneto_end)
        self.lineEdit_head_end.setObjectName(u"lineEdit_head_end")

        self.gridLayout_5.addWidget(self.lineEdit_head_end, 3, 2, 1, 1)

        self.label_magnetometer_end = QLabel(self.groupBox_megneto_end)
        self.label_magnetometer_end.setObjectName(u"label_magnetometer_end")
        self.label_magnetometer_end.setPixmap(QPixmap(u":/icons/magnetometer 3 axes.png"))

        self.gridLayout_5.addWidget(self.label_magnetometer_end, 0, 0, 3, 1)

        self.label_Head_end = QLabel(self.groupBox_megneto_end)
        self.label_Head_end.setObjectName(u"label_Head_end")
        self.label_Head_end.setPixmap(QPixmap(u":/icons/compass.png"))

        self.gridLayout_5.addWidget(self.label_Head_end, 3, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_megneto_end, 2, 2, 1, 3)

        self.timeEdit_time_end = QTimeEdit(self.end_of_day)
        self.timeEdit_time_end.setObjectName(u"timeEdit_time_end")

        self.gridLayout_4.addWidget(self.timeEdit_time_end, 1, 3, 1, 2)


        self.verticalLayout_4.addWidget(self.end_of_day)

        icon3 = QIcon()
        icon3.addFile(u":/icons/sunset 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.end, icon3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        self.menuconfiguration = QMenu(self.menubar)
        self.menuconfiguration.setObjectName(u"menuconfiguration")
        self.menu_actions = QMenu(self.menubar)
        self.menu_actions.setObjectName(u"menu_actions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font = QFont()
        font.setFamilies([u"Roboto"])
        self.statusbar.setFont(font)
        self.statusbar.setAutoFillBackground(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_actions.menuAction())
        self.menubar.addAction(self.menuconfiguration.menuAction())
        self.menuconfiguration.addAction(self.action_USB_setting)
        self.menuconfiguration.addAction(self.action_Date_et_heure)
        self.menuconfiguration.addAction(self.action_Unit)
        self.menu_actions.addAction(self.actionTest_de_connection)
        self.menu_actions.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Solar Tracker setting", None))
        self.action_USB_setting.setText(QCoreApplication.translate("MainWindow", u"USB", None))
        self.action_Date_et_heure.setText(QCoreApplication.translate("MainWindow", u"Date et heure", None))
        self.action_Unit.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9s", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionTest_de_connection.setText(QCoreApplication.translate("MainWindow", u"Test de connection", None))
#if QT_CONFIG(tooltip)
        self.date_time.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_locale.setText("")
        self.label_solar_tracker.setText("")
        self.label_time.setText("")
        self.label_date.setText("")
        self.read_data_rtc_action.setText(QCoreApplication.translate("MainWindow", u"Lire les donn\u00e9es du Solar Tracker", None))
        self.write_data_rtc_action.setText(QCoreApplication.translate("MainWindow", u"\u00c9crire les donn\u00e9es vers le Solar Tracker", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.date_time), QCoreApplication.translate("MainWindow", u"RTC", None))
        self.start_of_day.setTitle(QCoreApplication.translate("MainWindow", u"D\u00e9but de journ\u00e9e", None))
        self.label_date_start.setText("")
        self.read_data_start_action.setText(QCoreApplication.translate("MainWindow", u"Lire les donn\u00e9es", None))
        self.label_time_start.setText("")
        self.groupBox_magneto_start.setTitle(QCoreApplication.translate("MainWindow", u"Orientation magnetom\u00e8tre", None))
        self.label_Y_start.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_X_start.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_Z_start.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_magnetometer_start.setText("")
        self.label_head_start.setText("")
        self.groupBox_servo_start.setTitle(QCoreApplication.translate("MainWindow", u"Servo Tilt up/down", None))
        self.label_servo_start.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.start), QCoreApplication.translate("MainWindow", u"Lev\u00e9", None))
        self.end_of_day.setTitle(QCoreApplication.translate("MainWindow", u"Fin de journ\u00e9e", None))
        self.read_data_end_action.setText(QCoreApplication.translate("MainWindow", u"Lire les donn\u00e9es", None))
        self.label_date_end.setText("")
        self.label_time_end.setText("")
        self.servo_end.setTitle(QCoreApplication.translate("MainWindow", u"Servo Tilt up/down", None))
        self.label_servo_end.setText("")
        self.groupBox_megneto_end.setTitle(QCoreApplication.translate("MainWindow", u"Orientation magnetom\u00e8tre", None))
        self.label_Y_end.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_X_end.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_Z_end.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_magnetometer_end.setText("")
        self.label_Head_end.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.end), QCoreApplication.translate("MainWindow", u"Couch\u00e9", None))
        self.menuconfiguration.setTitle(QCoreApplication.translate("MainWindow", u"Configurer", None))
        self.menu_actions.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

