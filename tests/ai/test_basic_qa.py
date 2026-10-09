import pytest

from ai.evaluator import Evaluator
import conftest

@pytest.mark.ai
@pytest.mark.parametrize("case", conftest.basic_qa_cases())

def test_basic_qa(llm_client, case):

    response = llm_client.generate(case["prompt"])  

    assert Evaluator.not_empty(response)

    assert Evaluator.contains(
        response,
        case["expected"]
    )
