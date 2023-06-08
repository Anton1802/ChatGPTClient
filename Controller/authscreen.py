from View.authscreen import AuthScreenView


class AuthScreenController:
    def __init__(self, model):
        self.model = model
        self.view = AuthScreenView(controller=self, model=self.model)

    def get_screen(self):
        return self.view
