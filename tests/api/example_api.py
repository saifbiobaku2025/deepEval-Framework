from api.http_client import HttpClient


class ExampleApi:

    def __init__(self, client: HttpClient):
        self.client = client

    def health(self):
        return self.client.get("/status/200")