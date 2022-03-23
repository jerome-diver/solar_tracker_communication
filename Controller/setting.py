"""Setting: Date and Time, USB device and port and so on..."""


class Setting:

    def __init__(self):
        """Setting RTC Controller need a model and a view to be runnable"""
        pass

    def use_model(self, model):
        """Use this model"""
        self.model = model

    def use_view(self, view):
        """Use this view"""
        self.view = view

