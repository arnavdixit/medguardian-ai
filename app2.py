import streamlit as st
from src.utils.chat_utils import start_conversation, handle_user_query
from src.utils.history_io import get_patient_history_file
from src.utils.base_functions import run_phx

run_phx()

st.title("Medical Chatbot")
st.markdown("This app provides a ChatGPT-like chatbot interface along with a sidebar to fetch patient history.")

number = "johnathan"
initial_query = (
    f"Please provide the patient's full medical history, including details of previous diagnoses, treatment plans, surgical interventions, medication regimens, allergies, immunizations, and other critical clinical information in the following format only:\n"
        '{\n'
        '  "Name": "Provide the patient\'s full name",\n'
        '  "Age": "Provide the patient\'s age",\n'
        '}\n'
    )

if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = None

# Sidebar: Patient lookup with dynamic input and submit button using a form
with st.sidebar:
    st.header("Patient Lookup")
    with st.form("lookup_form"):
        medical_ref = st.text_input("Enter Medical Reference Number")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            file_path = get_patient_history_file(medical_ref)
            result = start_conversation(file_path, initial_query)
            st.session_state.agent = result["agent"]
            response = result["response"]
            st.markdown("### Patient History")
            st.text_area("Patient History", response, height=300)
        
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
if prompt := st.chat_input("Enter your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Retrieve agent from session state
    agent = st.session_state.get("agent")
    if agent is None:
        st.error("Please load a patient record first by entering a Medical Reference Number.")
    else:
        with st.chat_message("assistant"):
            stream = handle_user_query(agent, prompt)
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})