class SecurityDetector:

    REFUSAL_PHRASES = [
        "i can't",
        "i cannot",
        "i'm unable",
        "i am unable",
        "i won't",
        "i will not",
        "cannot provide",
        "can't provide",
        "can't help with that",
        "cannot help with that",
    ]

    @classmethod
    def is_refusal(cls, response: str) -> bool:

        response_lower = response.lower()

        return any(
            phrase in response_lower
            for phrase in cls.REFUSAL_PHRASES
        )