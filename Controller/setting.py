"""Setting: Date and Time, USB device and port and so on..."""


class Setting:

    def __init__(self):
        """Setting RTC Controller need a model and a view to be runnable"""
        self._model = None
        self._view = None

    @property
    def model(self, model) -> None:
        """model property getter"""
        self._model = model

    def view(self, view) -> None:
        """view property getter"""
        self._view = view

