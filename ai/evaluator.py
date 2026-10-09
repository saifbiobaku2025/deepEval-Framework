class Evaluator:

    @staticmethod
    def contains(response: str, expected: str) -> bool:
        return expected.lower() in response.lower()

    @staticmethod
    def not_empty(response: str) -> bool:
        return bool(response.strip())

    @staticmethod
    def max_length(response: str, maximum: int) -> bool:
        return len(response) <= maximum