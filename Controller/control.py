"""Main root Controller
All the other dedicated controllers are child of this Controller"""

from PySide6.QtCore import QObject, Signal, Slot

from Controller.setting import Setting
from Controller.communicate import Communicate
from Controller.views_actions import ViewsActions


class Control:
    """Main Controller"""



    def __init__(self):
        self._communication = None
        self._setting = None
        self._views_actions = None

    @property
    def views_actions(self):
        """views_actions property getter"""
        return self._views_actions

    @views_actions.setter
    def views_actions(self, main_ui):
        """views_actions setter"""
        self._views_actions = ViewsActions(main_ui)

    @property
    def setting(self):
        """setting property getter"""
        return self._setting

    @setting.setter
    def setting(self, config_ui):
        """setting setter"""
        self._setting = Setting()

    @property
    def communication(self):
        """communication property getter"""
        return self._communication

    @communication.setter
    def communication(self, main_view):
        """communication setter"""
        self._communication = Communicate(main_view)
