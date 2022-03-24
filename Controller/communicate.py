"""Communication via USB with Arduino Solar Tracker for:
    1/ set date and time
    2/ get morning start data collected
    3/ get evening end data collected
"""

from serial import Serial


class Communicate:
    """through USB"""
    def __init__(self):
        self._view = None
        self._model_rtc = None
        self._model_magnetometer = None
        self._model_eeprom = None
        self.arduino = Serial()
        self.arduino.baudrate = 9600

    @property
    def view(self):
        """view property getter"""
        return self._view

    @view.setter
    def view(self, ui):
        """view setter"""
        self._view = ui

    @property
    def model_rtc(self):
        """RTC model getter"""
        return self._model_rtc

    @model_rtc.setter
    def model_rtc(self, model):
        """RTC model"""
        self._model_rtc = model

    @property
    def model_magnetometer(self):
        """Magnetometer model getter"""
        return self._model_magnetometer

    @model_magnetometer.setter
    def model_magnetometer(self, model):
        """Magnetometer model setter"""
        self.model_magnetometer = model

    @property
    def model_eeprom(self):
        """EEPROM model getter"""
        return self._model_eeprom

    @model_eeprom.setter
    def model_eeprom(self, model):
        """EEPROM model setter"""
        self._model_eeprom = model

    @property
    def port(self):
        """Arduino USB port getter"""
        return self.arduino.port

    @port.setter
    def port(self, p):
        """Set Arduino USB port"""
        self.arduino.port = p

    def test(self):
        """Test communication with Arduino"""
        self.arduino.open()
        self.arduino.write(b'Test')

