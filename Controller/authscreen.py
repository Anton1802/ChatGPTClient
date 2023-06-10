from View.authscreen import AuthScreenView


class AuthScreenController:
    def __init__(self, model):
        self.model = model
        self.view = AuthScreenView(controller=self, model=self.model, name="authscreen")

    def get_screen(self):
        return self.view

    def set_token(self, token: str):
        status = self.model.set_token(token)
        if status:
            self.view.open_popup("Info", "Token saved!")
        else:
            self.view.open_popup("Error", "Token not saved!")
