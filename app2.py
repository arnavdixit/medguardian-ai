import streamlit as st
from src.utils.chat_utils import start_conversation

st.title("Medical Chatbot")
st.markdown("This app provides a ChatGPT-like chatbot interface along with a sidebar to fetch patient history.")

number = "johnathan"
initial_query = (
    f"Please provide the patient's {number} full medical history, including details of previous diagnoses, treatment plans, surgical interventions, medication regimens, allergies, immunizations, and other critical clinical information in the following format only:\n"
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

# Sidebar: Patient lookup with dynamic input and submit button using a form
with st.sidebar:
    st.header("Patient Lookup")
    with st.form("lookup_form"):
        medical_ref = st.text_input("Enter Medical Reference Number")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            patient_history = start_conversation(medical_ref)
            st.markdown("### Patient History")
            st.text_area("Patient History", patient_history, height=300)