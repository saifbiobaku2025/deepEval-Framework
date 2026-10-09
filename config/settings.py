import os

from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv(
    "BASE_URL",
    "https://example.com"
)

API_URL = os.getenv(
    "API_URL",
    "https://httpbin.org"
)

HEADLESS = os.getenv(
    "HEADLESS",
    "true"
).lower() == "true"


OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:latest"
)

OLLAMA_MODEL_QWEN = os.getenv(
    "OLLAMA_MODEL_QWEN",
    "qwen2.5:7b"
)