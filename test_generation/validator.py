class TestCaseValidator:

    REQUIRED_FIELDS = {
        "id",
        "category",
        "priority",
        "input",
        "expected_output",
        "tags",
    }

    VALID_PRIORITIES = {
        "critical",
        "high",
        "medium",
        "low",
    }

    @classmethod
    def validate(cls, test_case) -> None:

        missing = cls.REQUIRED_FIELDS - set(
            test_case.__dict__.keys()
        )

        if missing:
            raise ValueError(
                f"Missing fields: {missing}"
            )

        if test_case.priority not in cls.VALID_PRIORITIES:
            raise ValueError(
                f"Invalid priority: {test_case.priority}"
            )

        if not test_case.input.strip():
            raise ValueError("Test input cannot be empty")

        if not test_case.expected_output.strip():
            raise ValueError(
                "Expected output cannot be empty"
            )