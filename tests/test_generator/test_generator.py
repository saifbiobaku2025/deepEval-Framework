import pytest

from test_generation.generator import AITestGenerator
from test_generation.validator import TestCaseValidator


@pytest.mark.ai
def test_generate_test_cases(llm_client):

    generator = AITestGenerator(llm_client)

    requirement = """
    A user should be able to reset their password
    using their registered email address.
    """

    test_cases = generator.generate(requirement)

    assert test_cases
    assert len(test_cases) >= 3

    for test_case in test_cases:
        TestCaseValidator.validate(test_case)