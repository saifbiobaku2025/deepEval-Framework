from deepeval.metrics import (
    AnswerRelevancyMetric,
    GEval,
    HallucinationMetric,
)
from deepeval.test_case import SingleTurnParams


def answer_relevancy(threshold=0.7, eval_model=None):
    return AnswerRelevancyMetric(
        threshold=threshold,
        include_reason=True,
        verbose_mode=True,
        model=eval_model
    )

def hallucination(threshold=0.8, eval_model=None):
    return HallucinationMetric(
        threshold=threshold,
        include_reason=True,
        verbose_mode=True,
        model=eval_model
    )


def correctness(threshold=0.8, eval_model=None):
    return GEval(
        name="Correctness",
        criteria="""
        Determine whether the actual answer correctly answers
        the user's question and agrees with the expected answer.
        Penalize factual errors and contradictions.
        """,
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT,
        ],
        threshold=threshold,
        model=eval_model, # ← Ollama evaluator
        verbose_mode=True, # ← helpful for debugging# You can set your evaluation model here if needed
    )