from ai.models import EvaluationResult


class AIQualityGate:

    def check(self, results: list[EvaluationResult]) -> None:

        failures = [
            result
            for result in results
            if not result.passed
        ]

        if failures:
            messages = [
                f"{r.metric}: {r.score:.2f} < {r.threshold:.2f}"
                for r in failures
            ]

            raise AssertionError(
                "AI quality gate failed:\n"
                + "\n".join(messages)
            )
