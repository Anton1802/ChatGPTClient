import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from Utility.observer import Observer

class MainScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        pass


Builder.load_file(os.path.join(os.path.join(os.path.dirname(__file__), "mainscreen.kv")))
