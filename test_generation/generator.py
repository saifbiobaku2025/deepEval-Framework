import json
from re import match
import re

from ai.client import LLMClient
from test_generation.models import GeneratedTestCase


class AITestGenerator:

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def generate(self, requirement: str) -> list[GeneratedTestCase]:

        prompt = f"""
              You are an enterprise QA test engineer.

              Generate test cases for the following requirement:

              {requirement}

              Generate:
              - happy path tests
              - negative tests
              - edge cases
              - boundary cases

              Return ONLY valid JSON.

              Do not add:
              - explanations
              - markdown
              - code fences
              - notes

              Schema:
              [
                {{
                  "id": "generated-001",
                  "category": "functional",
                  "priority": "high",
                  "input": "...",
                  "expected_output": "...",
                  "tags": ["generated", "regression"]
                }}
              ]
              """

        response = self.llm_client.generate(prompt)

        print(f"RAW RESPONSE: {repr(response)}")

        if not response:
          raise ValueError("LLM returned empty response")

        # data = json.loads(response)
        data = self.extract_json(response)

        return [
            GeneratedTestCase(**test_case)
            for test_case in data
        ]

    def extract_json(self, response: str):
        match = re.search(r"\[[\s\S]*\]", response)

        if not match:
            raise ValueError(
                f"No JSON array found in response:\n{response}"
            )

        return json.loads(match.group(0))