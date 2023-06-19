import os
from typing import Generator

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

from Utility.observer import Observer

from kivy.clock import Clock


class ProgressPopup(Popup):
    pass


class AskPopup(Popup):
    text_label = ObjectProperty()


class MainScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    popup = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        if self.model.response[0] != None:
            response: Generator[str, None, None] = self.model.response[0]
            response_text = ""
            for word in response:
                response_text += word
            self.ids.label_output.text = response_text
        else:
            Clock.schedule_once(lambda x: self.show_popup("Error", "TextField empty!"))
    
    def send_click_button(self) -> None:
        text = self.ids.text_input_request.text 
        self.controller.set_request(text)

    def logout_click_yes(self) -> None:
        self.controller.logout()
        self.popup.dismiss()

    def logout_click_no(self) -> None:
        self.popup.dismiss()

    def logout_click_button(self) -> None:
        self.popup = AskPopup(
            title="Ask",
            text_label="You want to log out?",
            auto_dismiss=False,
        )

        btn_yes = self.popup.ids.btn_yes
        btn_no = self.popup.ids.btn_no

        btn_yes.bind(on_press=lambda x: self.logout_click_yes())
        btn_no.bind(on_press=lambda x: self.logout_click_no())

        self.popup.open()

    def show_progress_popup(self) -> None:
        self.popup = ProgressPopup()
        self.popup.open()

    def show_popup(self, title: str, text: str) -> None:
        self.popup = Popup(
            title=title,
            content=Label(text=text),
            size_hint=(0.5, 0.2),
        )
        self.popup.open()


Builder.load_file(os.path.join(os.path.join(os.path.dirname(__file__), "mainscreen.kv")))
