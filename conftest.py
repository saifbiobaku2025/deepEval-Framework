import json

import pytest
from playwright.sync_api import Page
from pages.example_page import ExamplePage
from tests.api.http_client import HttpClient
from tests.api.example_api import ExampleApi
from ai.client import LLMClient
from config.settings import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
    OLLAMA_MODEL_QWEN,  
)
import ollama
from deepeval.models import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric

from observability.tracing import setup_tracing
setup_tracing()


@pytest.fixture
def app_page(page: Page):
	page.goto("https://example.com")
	return page

@pytest.fixture
def example_api():
    client = HttpClient("https://httpbin.org")
    return ExampleApi(client)

@pytest.fixture
def example_page(page):
    example = ExamplePage(page)
    example.open()

    return example


@pytest.fixture
def llm_client():

    return LLMClient(
        base_url=OLLAMA_BASE_URL,
        model=OLLAMA_MODEL,
        # model=OLLAMA_MODEL_QWEN,
    )

def basic_qa_cases():
    return cases
with open(
    "data/ai/basic_qa.json",
    encoding="utf-8"
) as file:
    cases = json.load(file)


class OllamaEvalModel(DeepEvalBaseLLM):
    def __init__(self, model_name: str, base_url: str = OLLAMA_BASE_URL):
        self.model_name = model_name
        self.base_url = base_url
        self.client = ollama.Client(host=base_url)

    def load_model(self):
        return self.client

    def generate(self, prompt: str) -> str:
        response = self.client.generate(model=self.model_name, prompt=prompt)
        return response.get("response", "")

    async def a_generate(self, prompt: str) -> str:
        # DeepEval executes metrics asynchronously
        return self.generate(prompt)

    def get_model_name(self) -> str:
        return self.model_name


@pytest.fixture
def eval_model():
    """Provides a DeepEval-compatible local Ollama wrapper instance."""
    return OllamaEvalModel(model_name=OLLAMA_MODEL_QWEN, base_url=OLLAMA_BASE_URL)