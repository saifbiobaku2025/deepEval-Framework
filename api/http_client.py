import requests


class HttpClient:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.get(url, **kwargs)

    def post(self, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.post(url, **kwargs)
