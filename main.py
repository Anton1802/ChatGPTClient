from kivy.app import App

class ChatGPTClient(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        pass

if __name__ == "__main__":
    ChatGPTClient().run()
