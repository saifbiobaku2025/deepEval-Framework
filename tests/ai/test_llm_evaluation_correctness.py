import pytest

from deepeval.test_case import LLMTestCase
from deepeval.metrics import GEval
from deepeval.test_case import SingleTurnParams


@pytest.mark.ai
def test_answer_correctness(llm_client, eval_model):
    prompt = "What is the capital of France?"
    response = llm_client.generate(prompt)

    test_case = LLMTestCase(
        input=prompt,
        actual_output=response,
        expected_output="The capital of France is Paris.",
    )

    correctness = GEval(
    name="Correctness",
    criteria="""
    Determine whether the actual answer correctly answers
    the user's question and agrees with the expected answer.
    Penalize factual errors or contradictions.
    """,
    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    threshold=0.8,
    model=eval_model, # ← Ollama evaluator
    verbose_mode=True, # ← helpful for debugging
)

    correctness.measure(test_case)

    print(f"Correctness score: {correctness.score}")
    print(f"Correctness reason: {correctness.reason}")

    assert correctness.score >= 0.8