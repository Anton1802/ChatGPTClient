import os
from typing import Generator

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
        response: Generator[str, None, None] = self.model.response
        response_text = ""
        for word in response:
            response_text += word
        self.ids.label_output.text = response_text
    
    def send_click_button(self) -> None:
        text = self.ids.text_input_request.text 
        self.controller.set_request(text)

Builder.load_file(os.path.join(os.path.join(os.path.dirname(__file__), "mainscreen.kv")))
