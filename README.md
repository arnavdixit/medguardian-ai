# MedGuardian.AI

MedGuardian.AI is an AI-driven chat assistant designed for healthcare applications. It integrates patient information retrieval with interactive chat capabilities to help medical professionals and patients access critical data quickly. This branch (dev-aayush) includes ongoing development and enhancements related to patient information queries and a streamlined chat interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Overview

MedGuardian.AI leverages Streamlit to provide a dynamic, web-based chat interface. It uses custom modules (e.g., `query`) to fetch patient information and process user queries. The application is structured to support a conversational UI where users can enter their unique patient ID (UHR) and ask questions, with responses generated in real time.

## Features

- **Patient Information Integration:**  
  Enter a UHR (Unique Health Record) ID via the sidebar to fetch and display patient details.
- **Interactive Chat Interface:**  
  Users can ask questions using a chat input, and the bot responds based on stored patient data and predefined logic.
- **Suggested Questions:**  
  The interface includes a set of suggested questions to help guide the user.
- **Modular Design:**  
  Key functionalities such as fetching basic patient information and processing queries are abstracted into separate modules (`basic_info`, `user_query`).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/arnavdixit/medguardian-ai.git
   cd medguardian-ai
   git checkout dev-aayush

2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

## Usage
To run the MedGuardian.AI application locally, use the following command. This command will start the Streamlit server and open the chat interface in your default web browser. In the sidebar, enter the patient's UHR ID and click "Fetch Patient Info" to retrieve patient details. Then, use the main chat panel to ask questions. The chat interface is designed to pass both the user prompt and UHR to the response_generator function for generating responses.

```bash
streamlit run app.py
