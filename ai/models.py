from dataclasses import dataclass


@dataclass
class EvaluationResult:
    test_id: str
    metric: str
    score: float
    threshold: float
    passed: bool
    reason: str = ""