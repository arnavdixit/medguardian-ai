from src.utils.chat_utils import start_conversation, handle_user_query
from src.utils.history_io import get_patient_history_file, get_patient_name
# =============================================================================
# Main execution flow
# =============================================================================
if __name__ == "__main__":
    # Fetch Name
    name = "Jhonathon Doe"
    
    # Define the initial query in a legitimate JSON format
    def initial_query(name):
        query = (
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
        return query
    
    # Start the conversation with the initial query
    id = input("Enter the patient's ID: ")
    history_file = get_patient_history_file(id)
    patient_name = get_patient_name(history_file)
    result = start_conversation(history_file, initial_query(patient_name))
    agent = result["agent"]
    response = result["response"]
    print("Agent:", response)
    inp = input("User: ")
    while inp != "exit":
        response = handle_user_query(agent, inp).response
        print("Agent:", response)
        inp = input("User: ")