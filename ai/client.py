# import requests


# class LLMClient:

#     def __init__(self, base_url: str, model: str):
#         self.base_url = base_url.rstrip("/")
#         self.model = model

#     def generate(self, prompt: str) -> str:

#         response = requests.post(
#             f"{self.base_url}/api/generate",
#             json={
#                 "model": self.model,
#                 "prompt": prompt,
#                 "stream": False,
#             },
#             timeout=120,
#         )

#         response.raise_for_status()

#         return response.json()["response"]



import ollama


class LLMClient:

    def __init__(self, base_url: str, model: str):
        self.model = model

    def generate(self, prompt: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        return response["message"]["content"]