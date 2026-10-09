from urllib import response

import pytest

from deepeval import assert_test
from deepeval.test_case import LLMTestCase

from ai.deepeval_metrics import (
    answer_relevancy,
    correctness,
    hallucination,  
)

@pytest.mark.ai
def test_llm_quality(llm_client, eval_model): 

    prompt = "What is the capital of France?"

    response = llm_client.generate(prompt)

    test_case = LLMTestCase(
        input=prompt,
        actual_output=response,
        expected_output="The capital of France is Paris",
    )

    metrics = [
        answer_relevancy(threshold=0.7, eval_model=eval_model),
        correctness(threshold=0.8, eval_model=eval_model),
    ]


    for metric in metrics:
        metric.measure(test_case)

        print("\n" + "=" * 70)
        print(metric.__class__.__name__)

        if hasattr(metric, "score"):
            print(f"Score: {metric.score}")

        if hasattr(metric, "reason"):
            print(f"Reason: {metric.reason}")

        assert metric.score >= metric.threshold
@pytest.mark.ai
def test_llm_hallucination(llm_client, eval_model):

    context = [
        "The company provides technical support from Monday through Friday.",
        "Support hours are 8 AM to 6 PM Eastern Time."
    ]

    prompt = f"""
    Using only the information below, answer the question.

    Context:
    {" ".join(context)}

    Question:
    When can I get technical support from the company?
    """

    response = llm_client.generate(prompt)

    print("\nActual Output:")
    print(response)

    test_case = LLMTestCase(
        input=prompt,
        actual_output=response,
        context=context,
    )

    metrics = [
        hallucination(threshold=0.8, eval_model=eval_model),
    ]

    for metric in metrics:
        metric.measure(test_case)

        print("\n" + "=" * 70)
        print(metric.__class__.__name__)
        print(f"Score: {metric.score}")
        print(f"Reason: {metric.reason}")

        assert metric.score >= metric.threshold