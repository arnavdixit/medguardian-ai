from query import basic_info, user_query

import streamlit as st
from src.utils.chat_utils import *

# Set up layout
st.set_page_config(layout="wide")

def reset_session_state():
    st.session_state["chat_history"] = []
    st.session_state["suggested_ques"] = ["q1", "q2", "q3"]
    st.session_state["patient_info"] = None
    st.session_state["chat_input"] = ""

def ask_ques():
    if "patient_info" in st.session_state and st.session_state["patient_info"] and "uhr" in st.session_state["patient_info"]:
        res = user_query(st.session_state["chat_input"], st.session_state["patient_info"]["uhr"])
        print(res)
        st.session_state["chat_history"].append(("ai", res["response_to_user_query"]))
        st.session_state["suggested_ques"] = res["suggested_follow_up"]
    else:
        st.session_state["chat_history"].append(("ai", "Enter a valid UHR!"))
        print("not valid uhr")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "suggested_ques" not in st.session_state:
    st.session_state["suggested_ques"] = ["q1", "q2", "q3"]
if "patinet_info" not in st.session_state:
    st.session_state["patient_info"] = None
if "chat_input" not in st.session_state:
    st.session_state["chat_input"] = ""

# Left panel: UHR input and patient information
with st.sidebar:
    st.header("Patient UHR Input")
    uhr_id = st.text_input("Enter UHR ID")
    if st.button("Fetch Patient Info"):
        #reset_session_state()

        res = basic_info(uhr_id)
        if "error" in res:
            st.write(res["error"])
        else:
            st.session_state["patient_info"] = res
    
    if st.session_state["patient_info"]:
        st.subheader("Patient Information")
        for key, value in st.session_state["patient_info"].items():
            st.write(f"**{key}:** {value}")

# Chat layout
col1, col2 = st.columns([3, 7])

# Chat display area
with col2:
    st.header("MedGuardian.AI")

    chat_container = st.container()
    with chat_container:
        if "chat_history" in st.session_state and st.session_state["chat_history"]:
            chat_history_html = ""
            for role, message in st.session_state["chat_history"]:
                if role == "user":
                    chat_history_html += f"<div style='text-align: right; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin: 5px 0;'>{message}</div>"
                elif role == "ai":
                    chat_history_html += f"<div style='text-align: left; background-color: #E8E8E8; padding: 10px; border-radius: 10px; margin: 5px 0;'>{message}</div>"
            st.markdown(f"<div style='max-height: 400px; overflow-y: auto;'>{chat_history_html}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Suggested Questions")
    cols = st.columns(3)
    for i, question in enumerate(st.session_state["suggested_ques"]):
        if cols[i].button(question):
            st.session_state["chat_input"] = question
            ask_ques()

    # Chat input
    st.session_state["chat_input"] = st.text_input("Type your message", key=st.session_state["chat_input"])
    if st.button("Send Message"):
        print(st.session_state["chat_input"])
        if st.session_state["chat_input"]:
            print("asking chat gpt")
            ask_ques()