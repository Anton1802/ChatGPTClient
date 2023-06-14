import requests
import json
import multitasking

class OpenAIClient:
    def __init__(self, api_key: str, timeout: int) -> None:
        self.__api_key = api_key
        self.__api_host = "https://api.openai.com"
        
        self.__timeout = timeout

    @multitasking.task
    def request(
        self, 
        messages: list[dict[str, str]],
        model: str = "gpt-3.5-turbo",
        temperature: float = 1,
        top_probability: float = 1,
        response_message: list = [None]
    ) -> None:
        data = {
            "messages": messages,
            "model": model,
            "temperature": temperature,
            "top_p": top_probability,
            "stream": True,
        }
        endpoint = f"{self.__api_host}/v1/chat/completions"
        response = requests.post(
            endpoint,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.__api_key}",
            },
            json=data,
            timeout=self.__timeout
        )
        response.raise_for_status()
        
        def gen(response):
            for line in response.iter_lines():
                data = line.lstrip(b"data: ").decode("utf-8")
                if data == "[DONE]":
                    break
                if not data:
                    continue
                data = json.loads(data)
                delta = data["choices"][0]["delta"]
                if "content" not in delta:
                    continue
                yield delta["content"]
        
        response_message.append(gen(response))
