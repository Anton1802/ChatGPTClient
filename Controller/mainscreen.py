import multitasking
import time

from View.mainscreen import MainScreenView


class MainScreenController:
    def __init__(self, model, sm):
        self.model = model
        self.view = MainScreenView(controller=self, model=self.model, name="mainscreen")
        self.sm = sm 

    def get_screen(self):
        return self.view

    def set_request(self, message: str):
        self.model.send_request(message)
        self.view.show_progress_popup()

        @multitasking.task
        def check_progressbar(view, model):
            while True:
                time.sleep(1)
                if view.popup.ids.response_progress_bar.value != 1:
                    view.popup.ids.response_progress_bar.value += .2
                else:
                    view.popup.ids.response_progress_bar.value = 0

                if len(model.response) > 0:
                    model.notify_observers()
                    break

            view.popup.dismiss()
            
        check_progressbar(self.view, self.model)

        self.view.ids.text_input_request.text = ""

    def logout(self):
        if self.model.remove_token():
            self.sm.current = "authscreen"
