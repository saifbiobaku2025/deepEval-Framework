from ai.evaluator import Evaluator

def test_llm_response(llm_client):

    response = llm_client.generate(
        "What is the capital of France?"
    )

    assert Evaluator.not_empty(response)
    assert Evaluator.contains(response, "Paris")