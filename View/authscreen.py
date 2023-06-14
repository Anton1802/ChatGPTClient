import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

from Utility.observer import Observer

class Apopup(Popup):
    text = StringProperty()

class AuthScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.popup = None

    def model_is_changed(self):
        pass

    def login_click_button(self):
        input_text = self.ids.token_text_input.text
        self.controller.set_token(input_text)

    def open_popup(self, title: str, text: str):
        self.popup = Apopup(
            title=title,
            text=text,
        )
        self.popup.open()

Builder.load_file(os.path.join(os.path.join(os.path.dirname(__file__), "authscreen.kv")))
