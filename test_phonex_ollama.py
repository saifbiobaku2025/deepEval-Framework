from phoenix.otel import register
from openinference.instrumentation.ollama import OllamaInstrumentor
import ollama


tracer_provider = register(
    project_name="enterprise-ai-test-platform",
    endpoint="http://localhost:6006/v1/traces",
)

OllamaInstrumentor().instrument(
    tracer_provider=tracer_provider
)


response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(response["message"]["content"])