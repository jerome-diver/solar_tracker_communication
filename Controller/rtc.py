# RTC Timer setting: Date and Time


class Setting:

    def __init__(self, model, view):
        """Setting RTC Controller need a model and a view to be runnable"""
        self._date = ""
        self._time = ""
        self._model = model
        self._view = view

