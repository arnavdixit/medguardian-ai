# %%
# Import phoenix and tracing modules
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from phoenix.otel import register

def run_phx():
    import phoenix as px
    session = px.launch_app()
    tracer_provider = register()
    LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)


