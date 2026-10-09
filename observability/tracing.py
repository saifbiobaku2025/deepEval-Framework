from phoenix.otel import register
from openinference.instrumentation.ollama import OllamaInstrumentor


def setup_tracing():

    tracer_provider = register(
        project_name="enterprise-ai-test-platform",
        endpoint="http://localhost:6006/v1/traces",
    )

    OllamaInstrumentor().instrument(
        tracer_provider=tracer_provider
    )

    return tracer_provider