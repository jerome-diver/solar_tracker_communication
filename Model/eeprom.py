# Model for Arduino EEPROM specific contents
# Content can be:
#   _ Morning last time and date & magnetometer coordinates & tilt servo angle
#   _ Evening last time and date & magnetometer coordinates & tilt servo angle
#   _ declinaison in radian or degree
#   _ last day total cumulated sun time

morning_address = 0x00
evening_address = 0x10


class EEPROM:
    """ Model for Arduino EEPROM specific contents
        Content can be:
        _ Morning last time and date & magnetometer coordinates & tilt servo angle
        _ Evening last time and date & magnetometer coordinates & tilt servo angle
        _ declinaison in radian or degree
        _ last day total cumulated sun time
    """
    def __init__(self):
        self._morning = 0