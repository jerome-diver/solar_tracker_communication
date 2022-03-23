"""Magnetometer Model for X, Y, Z axes and heading direction"""


class Magnetometer:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Z = 0
        self.heading = 0
        self.declinaison = 0
        self.unit = "degree"