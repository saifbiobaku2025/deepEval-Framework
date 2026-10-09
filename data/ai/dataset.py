import json
from pathlib import Path


class AITestDataset:

    def __init__(self, path: str):
        self.path = Path(path)

    def load(self) -> list[dict]:
        with self.path.open("r", encoding="utf-8") as file:
            return json.load(file)