import json
from pathlib import Path
from typing import Generator

from Utility.client import OpenAIClient

class MainScreenModel:
    def __init__(self) -> None:
        self._observers = []
        self.__path_token = Path('Config', 'token.json') 
        self.__response: Generator[str, None, None] 

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

    def send_request(self, message: str) -> None:
        with open(str(self.__path_token), 'r') as file:
            token = json.load(file)['token']
        
        client = OpenAIClient(token, 10)

        self.__response = client.request([{'role': 'user', "content": message}])

        self.notify_observers()
        
