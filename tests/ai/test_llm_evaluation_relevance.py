import pytest

from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase



@pytest.mark.ai
def test_answer_relevancy(llm_client, eval_model):

    prompt = "What is the capital of France?"

    response = llm_client.generate(prompt)

    test_case = LLMTestCase(
        input=prompt,
        actual_output=response,
    )

    metric = AnswerRelevancyMetric(
        threshold=0.7,
        include_reason=True,
        verbose_mode=True,
        model=eval_model
    )

    metric.measure(test_case)

    print(f"Metric score: {metric.score}")
    print(f"Metric reason: {metric.reason}")

    assert metric.score >= 0.7

