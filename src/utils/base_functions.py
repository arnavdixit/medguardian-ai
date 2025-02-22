# %%
# Import phoenix and tracing modules
import phoenix as px
session = px.launch_app()

from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from phoenix.otel import register

tracer_provider = register()
LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)


