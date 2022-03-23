"""Communication via USB with Arduino Solar Tracker for:
    1/ set date and time
    2/ get morning start data collected
    3/ get evening end data collected
"""

from serial import Serial


class Communicate:
    """through USB"""
    def __init__(self):
        self.view = None
        self.model_rtc = None
        self.model_magnetometer = None
        self.model_eeprom = None
        self.arduino = Serial()
        self.arduino.baudrate = 9600

    def use_view(self, view):
        self.view = view

    def use_model_rtc(self, model):
        """Use this model"""
        self.model_rtc = model

    def use_model_magnetometer(self, model):
        """Use this model"""
        self.model_magnetometer = model

    def use_model_eeprom(self, model):
        """Use this model"""
        self.model_eeprom = model

    def set_port(self, port):
        """Set USB port"""
        self.arduino.port = port

    def test(self):
        """Test communication with Arduino"""
        self.arduino.open()
        self.arduino.write(b'Test')

