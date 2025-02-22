from os import environ
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = environ["OPENAI_API_KEY"]

# %%
# Import necessary modules from llama_index and other libraries
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

# Create an LLM object to use for the QueryEngine and the ReActAgent.
llm = OpenAI(model="gpt-4")

# =============================================================================
# Function: setup_history_index
# =============================================================================
def setup_history_index(history_file: str, persist_dir: str = "./persisted_index/") -> VectorStoreIndex:
    """
    Sets up the history index from a provided history text file. If a persisted index exists,
    it loads that; otherwise, it creates a new index from the file and persists it.
    
    Args:
        history_file (str): Path to the file containing the patient's medical history.
        persist_dir (str): Directory where the index is to be persisted. Defaults to "./persisted_index/".
        
    Returns:
        VectorStoreIndex: The loaded or newly created history index.
    """
    index_loaded = False

    # Attempt to load the index from persisted storage
    try:
        storage_context = StorageContext.from_defaults(persist_dir=history_file)
        history_index = load_index_from_storage(storage_context)
        index_loaded = True
        print("Index successfully loaded from storage.")
    except Exception as e:
        print(f"Failed to load persisted index: {e}. Creating a new index.")

    # If the index is not loaded, read from the file and build the index
    if not index_loaded:
        history_docs = SimpleDirectoryReader(input_files=[history_file]).load_data()
        history_index = VectorStoreIndex.from_documents(history_docs, show_progress=True)
        history_index.storage_context.persist(persist_dir=persist_dir)
        print("New index created and persisted.")
    
    return history_index

# =============================================================================
# Function: create_query_engine_tool
# =============================================================================
def create_query_engine_tool(history_index: VectorStoreIndex) -> list:
    """
    Converts the history index into a query engine and creates a QueryEngineTool object.
    
    Args:
        history_index (VectorStoreIndex): The history index containing patient's records.
    
    Returns:
        list: A list containing a QueryEngineTool for the history engine.
    """
    # Convert the index into a query engine (using top 3 similar documents per query)
    history_engine = history_index.as_query_engine(similarity_top_k=3, llm=llm)
    
    # Create the QueryEngineTool with detailed metadata
    query_engine_tools = [
        QueryEngineTool(
            query_engine=history_engine,
            metadata=ToolMetadata(
                name="history",
                description=(
                    "Provides comprehensive access to a patient's complete medical history, including detailed records of previous diagnoses, treatment plans, "
                    "surgical interventions, medication regimens, allergies, immunizations, and other critical clinical information. "
                    "This tool is designed to assist healthcare providers, particularly in emergency settings, by delivering precise, plain text responses "
                    "based on well-formulated queries. When using this tool, please input a detailed question that clearly specifies the aspects of the "
                    "medical history you require—such as cardiac events, medication changes, surgical history, or chronic disease management—to ensure the "
                    "most relevant and targeted information is retrieved."
                ),
            ),
        )
    ]
    
    return query_engine_tools

# =============================================================================
# Function: initialize_agent
# =============================================================================
def initialize_agent(query_engine_tools: list, max_turns: int = 10, verbose: bool = True) -> ReActAgent:
    """
    Creates and returns a ReActAgent using the provided query engine tools.
    
    Args:
        query_engine_tools (list): A list of QueryEngineTool objects.
        max_turns (int): The maximum number of turns the agent will take in a conversation. Default is 10.
        verbose (bool): Enables detailed logging if set to True.
    
    Returns:
        ReActAgent: The initialized conversation agent.
    """
    agent = ReActAgent.from_tools(
        query_engine_tools,
        llm=llm,
        verbose=verbose,
        max_turns=max_turns,
    )
    return agent
