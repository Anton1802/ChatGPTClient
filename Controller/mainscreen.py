import multitasking
import time

from View.mainscreen import MainScreenView


class MainScreenController:
    def __init__(self, model):
        self.model = model
        self.view = MainScreenView(controller=self, model=self.model, name="mainscreen")

    def get_screen(self):
        return self.view

    def set_request(self, message: str):
        self.model.send_request(message)
        self.view.show_progress_popup()

        @multitasking.task
        def check_progressbar(view, model):
            while True:
                time.sleep(1)
                view.popup.ids.response_progress_bar.value += .01
                if len(model.response) > 0:
                    model.notify_observers()
                    break

            view.popup.dismiss()
            
        check_progressbar(self.view, self.model)
