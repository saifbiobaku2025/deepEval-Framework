import pytest

from deepeval import evaluate
from deepeval.test_case import LLMTestCase

from ai.models import EvaluationResult
from ai.quality_gate import AIQualityGate

from ai.deepeval_metrics import (
    correctness,
)

from openinference.instrumentation import using_attributes

import random

@pytest.mark.smoke
@pytest.mark.ai
def test_ai_quality_gate(llm_client, eval_model):

    prompt = "What is the capital of France?"
    expected = "The capital of France is Paris."
    with using_attributes(
        session_id=test_ai_quality_gate.__name__+"_"+str(random.randint(0, 100000000000)),
        metadata={
        "environment": "local",
        "prompt_version": "v1.0",
        "test_id": test_ai_quality_gate.__name__,
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
        test_id=test_ai_quality_gate.__name__,
        metric="correctness",
        score=metric.score,
        threshold=metric.threshold,
        passed=metric.score >= metric.threshold,
        reason=metric.reason or "",
    )

    AIQualityGate().check([evaluation])