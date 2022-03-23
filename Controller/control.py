"""Main root Controller
All the other dedicated controllers are child of this Controller"""

from setting import Setting
from communicate import Communicate

class Control:
    """Main Controller"""
    def __init__(self):
        self.communication = Communicate()
        self.setting = Setting()
