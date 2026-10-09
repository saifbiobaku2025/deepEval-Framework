import pytest

from data.ai.dataset import AITestDataset
from security.detectors import SecurityDetector
from security.models import SecurityResult


security_dataset = AITestDataset(
    "data/ai/security_dataset.json"
).load()

@pytest.mark.security
@pytest.mark.ai
@pytest.mark.prompt_injection
@pytest.mark.parametrize(
    "test_case",
    security_dataset,
    ids=[case["id"] for case in security_dataset],
)
def test_security_attack(llm_client, test_case):

    response = llm_client.generate(
        test_case["attack"]
    )

    passed = SecurityDetector.is_refusal(response)

    result = SecurityResult(
        test_id=test_case["id"],
        category=test_case["category"],
        severity=test_case["severity"],
        passed=passed,
        reason=(
            "Model safely refused attack"
            if passed
            else "Model did not clearly refuse attack"
        ),
    )

    assert result.passed, (
        f"{result.test_id} failed: "
        f"{result.reason}\n"
        f"Response: {response}"
    )