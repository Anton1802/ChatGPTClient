import json
import multitasking
from pathlib import Path

from Utility.client import OpenAIClient


class MainScreenModel:
    def __init__(self) -> None:
        self._observers = []
        self.__path_token = Path('Config', 'token.json') 
        self.__response: list = [] 

    @property
    def response(self):
        return self.__response

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for obj in self._observers:
            obj.model_is_changed()

    @multitasking.task
    def send_request(self, message: str) -> None:
        self.__response = []

        if len(message) <= 0:
            self.__response.append(None)
            return

        with open(str(self.__path_token), 'r') as file:
            token = json.load(file)['token']
        
        client = OpenAIClient(token, 10)

        client.request(
            messages=[{'role': 'user', 'content': message}],
            response_message=self.__response
        )
