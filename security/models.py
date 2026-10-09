from dataclasses import dataclass


@dataclass
class SecurityResult:
    test_id: str
    category: str
    severity: str
    passed: bool
    reason: str