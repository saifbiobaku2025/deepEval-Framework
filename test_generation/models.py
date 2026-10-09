from dataclasses import dataclass, field
from typing import Any

@dataclass
class GeneratedTestCase:
    id: str
    category: str
    priority: str
    input: dict[str, Any]
    expected_output: dict[str, Any]
    tags: list[str] = field(default_factory=list)