"""Communication via USB with Arduino Solar Tracker for:
    1/ set date and time
    2/ get morning start data collected
    3/ get evening end data collected
"""

from serial import Serial


class Communicate:
    """through USB"""
    def __init__(self):
        pass

    def use_view(self, view):
        self.view = view

    def use_model(self, model):
        """Use this model"""
        self.model = model

    def test(self):
        """Test communication with Arduino"""
        pass

