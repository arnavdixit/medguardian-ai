
from llama_index.core.agent import ReActAgent



# =============================================================================
# Function: handle_agent_response
# =============================================================================
def handle_agent_response(agent: ReActAgent, response: str) -> None:
    """
    Handles the agent's response by printing it and checking if the conversation is complete.
    If not complete, it prompts the user for the next input and continues the conversation.
    
    Args:
        agent (ReActAgent): The conversation agent.
        response (str): The current response from the agent.
    """
    print("Agent:", response)
    
    # if agent.is_conversation_complete():
    #     print("Conversation complete.")
    # else:
    #     pass
    #     # # Prompt the user for further input
    #     # user_input = input("User: ")
    #     # # Continue the conversation with the user's input
    #     # new_response = agent.continue_chat(user_input)
    #     # handle_agent_response(agent, new_response)

# =============================================================================
# Function: start_conversation
# =============================================================================
def start_conversation(agent: ReActAgent, initial_query: str) -> None:
    """
    Starts a conversation with the agent using the provided initial query.
    
    The initial query should be a detailed question in legitimate JSON format requesting the following details:
      - Name
      - Age
      - Gender
      - Allergies
      - Past Treatments with dates
      - Current Medication
      - Existing Health Condition
    
    Args:
        agent (ReActAgent): The conversation agent.
        initial_query (str): The initial query in plain text (formatted as valid JSON) to begin the conversation.
    """
    response = agent.chat(initial_query)
    return response
    # handle_agent_response(agent, response)

# =============================================================================
# Function: handle_user_query
# =============================================================================

def handle_user_query(agent: ReActAgent, user_query: str) -> None:

# Define the prompt for the agent including the request for follow-up questions in a static JSON format
    prompt = f"""
    {user_query}
    Please respond in the following JSON format:
    {{
        "response_to_user_query": "<agent response to the user query>",
        "suggested_follow_up": ["question1", "question2", "question3"]
    }}
    """

    # Get the response from the agent
    response = agent.chat(prompt)

    return response
    # Handle the agent's response
    # handle_agent_response(agent, response)
