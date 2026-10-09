from dataclasses import dataclass


@dataclass
class GeneratedTestCase:
    id: str
    category: str
    priority: str
    input: str
    expected_output: str
    tags: list[str]