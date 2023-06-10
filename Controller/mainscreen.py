from View.mainscreen import MainScreenView


class MainScreenController:
    def __init__(self, model):
        self.model = model
        self.view = MainScreenView(controller=self, model=self.model, name="mainscreen")

    def get_screen(self):
        return self.view
