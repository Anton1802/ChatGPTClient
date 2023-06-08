from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from Controller.authscreen import AuthScreenController
from Controller.mainscreen import MainScreenController
from Model.authscreen import AuthScreenModel
from Model.mainscreen import MainScreenModel

Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

Config.write()

class ChatGPTClient(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_auth = AuthScreenModel()
        self.model_main = MainScreenModel()

        self.controller_auth = AuthScreenController(self.model_auth)
        self.controller_main = MainScreenController(self.model_main)
        
        self.sm = ScreenManager()

    def build(self):
        self.sm.add_widget(self.controller_auth.get_screen())
        self.sm.add_widget(self.controller_main.get_screen())

        return self.sm 


if __name__ == "__main__":
    ChatGPTClient().run()
