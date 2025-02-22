from src.utils.setup import setup_history_index, create_query_engine_tool, initialize_agent
from src.utils.chat_utils import start_conversation
# =============================================================================
# Main execution flow
# =============================================================================
if __name__ == "__main__":
    # Set up the history index using the 'history.txt' file
    history_index = setup_history_index(history_file="rough/history.txt", persist_dir="./persisted_index/")
    
    # Create query engine tools based on the history index
    query_engine_tools = create_query_engine_tool(history_index)
    
    # Initialize the ReActAgent with the query engine tools
    agent = initialize_agent(query_engine_tools, max_turns=10, verbose=True)

    # Fetch Name
    name = "Jhonathon Doe"
    
    # Define the initial query in a legitimate JSON format
    initial_query = (
    f"Please provide the patient's {name} full medical history, including details of previous diagnoses, treatment plans, surgical interventions, medication regimens, allergies, immunizations, and other critical clinical information in the following format only:\n"
        '{\n'
        '  "Name": "Provide the patient\'s full name",\n'
        '  "Age": "Provide the patient\'s age",\n'
        '  "Gender": "Provide the patient\'s gender",\n'
        '  "Allergies": "List all known allergies",\n'
        '  "Current Medication": "List all current medications with dosage and frequency",\n'
        '  "Past Treatments": "Provide details of past treatments with corresponding dates",\n'
        '  "Past Surgeries": "Provide details of past surgeries and result with corresponding dates",\n'
        '  "Existing Health Condition": "Detail any existing health conditions"\n'
        '}\n'
    )
    
    # Start the conversation with the initial query
    start_conversation(agent, initial_query)
