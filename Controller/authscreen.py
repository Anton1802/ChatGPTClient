from View.authscreen import AuthScreenView

class AuthScreenController:
    def __init__(self, model, sm):
        self.model = model
        self.view = AuthScreenView(controller=self, model=self.model, name="authscreen")
        self.sm = sm

    def get_screen(self):
        return self.view

    def set_token(self, token: str):
        status = self.model.set_token(token)
        if status:
            self.view.open_popup("Info", "Token saved!")
            self.sm.current = "mainscreen"
        else:
            self.view.open_popup("Error", "Token not saved!")

    def is_auth(self):
        token = self.model.get_token()
        if token:
            return True
        return False
