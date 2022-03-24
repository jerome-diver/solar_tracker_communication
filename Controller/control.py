"""Main root Controller
All the other dedicated controllers are child of this Controller"""

from Controller.setting import Setting
from Controller.communicate import Communicate
from Controller.menu_actions import MenuActions


class Control:
    """Main Controller"""
    def __init__(self):
        self._communication = None
        self._setting = None
        self._menu_actions = None

    @property
    def menu_actions(self):
        """menu_actions property getter"""
        return self._menu_actions

    @menu_actions.setter
    def menu_actions(self, main_ui):
        """menu_actions setter"""
        self._menu_actions = MenuActions(main_ui)

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
    def communication(self, port):
        """communication setter"""
        self._communication = Communicate()
        self._communication.port(port)
