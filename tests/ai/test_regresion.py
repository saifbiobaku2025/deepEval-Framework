import random
import pytest

from openinference.instrumentation import using_attributes
from deepeval.test_case import LLMTestCase
from ai.models import EvaluationResult
from ai.quality_gate import AIQualityGate
from ai.deepeval_metrics import correctness

from data.ai.dataset import AITestDataset

dataset = AITestDataset(
    "data/ai/regression_dataset.json"
).load()

@pytest.mark.regression
@pytest.mark.ai
@pytest.mark.parametrize(
    "test_case",
    dataset,
    ids=[case["id"] for case in dataset],
)
def test_ai_regression(llm_client, test_case, eval_model):

    prompt = test_case["input"]
    expected = test_case["expected_output"]
    with using_attributes(
        session_id=test_ai_regression.__name__+"_"+str(random.randint(0, 100000000000)),
        metadata={
        "environment": "local",
        "prompt_version": test_case["prompt_version"],
        "model": test_case["model"],
        "category": test_case["category"],
        "test_id": test_case["id"]
        },
        ):
        response = llm_client.generate(prompt)

    test_case = LLMTestCase(
        input=prompt,
        actual_output=response,
        expected_output=expected,
    )

    metrics = [correctness(threshold=0.8, eval_model=eval_model)]

    for metric in metrics:
            metric.measure(test_case)

            print("\n" + "=" * 70)
            print(metric.__class__.__name__)

            if hasattr(metric, "score"):
                print(f"Score: {metric.score}")

            if hasattr(metric, "reason"):
                print(f"Reason: {metric.reason}")

            assert metric.score >= metric.threshold

    evaluation = EvaluationResult(
        test_id=test_ai_regression.__name__,
        metric="correctness",
        score=metric.score,
        threshold=metric.threshold,
        passed=metric.score >= metric.threshold,
        reason=metric.reason or "",
    )

    AIQualityGate().check([evaluation])