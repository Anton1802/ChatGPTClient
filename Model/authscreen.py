import json
import os
import re

from pathlib import Path

class AuthScreenModel:
    def __init__(self) -> None:
        self._observers = []
        self.__path_config = Path('Config')
        self.__path_token = Path(self.__path_config, 'token.json')

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        pass

    def _validate_token(self, token: str) -> bool:
        pattern = r'^sk-[a-zA-Z-0-9]{1,}$'
        if re.match(pattern, token):
            return True
        else:
            return False

    def set_token(self, token: str) -> bool:
        if not self._validate_token(token):
            return False

        if not os.path.exists(self.__path_token):
           with open(str(self.__path_token), 'w') as file:
               json.dump({"token": token}, file)
        else:
            with open(str(self.__path_token), 'r') as file:
                json_data = json.load(file)
                with open(str(self.__path_token), 'w') as file:
                    json_data['token'] = token
                    json.dump(json_data, file)

        return True
        
           
