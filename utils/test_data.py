import json
from pathlib import Path


def load_json(filename: str):
    path = Path("data") / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)