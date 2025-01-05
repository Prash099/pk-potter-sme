import streamlit as st
import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def load_lottie_local(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading Lottie file: {e}")
        return None

st.header("Welcome to Social Media Analyzer")

st.subheader("Send Data to Langflow API")

platform = st.text_input("What platform are you posting?")
post_type = st.text_input("Your post type?")


if st.button('Send to Langflow'):
    if platform and post_type:
        with st.spinner("Your report is being generated... Please wait!"):
        
            payload = {
                "input_value": "Hi, Give me a Report!",
                "output_type": "chat",
                "input_type": "chat",
                "tweaks": {
                    "File-jV8pD": {},
                    "SplitText-I29bE": {},
                    "AstraDB-yyuJm": {
                        "number_of_results": 200
                    },
                    "TextInput-ZTT93": {},
                    "ParseData-SYMXN": {},
                    "ChatOutput-PfRq9": {
                        "should_store_message": False
                    },
                    "Agent-sOIG2": {},
                    "ChatInput-mNEXC": {
                        "should_store_message": False
                    },
                    "CombineText-fr7QO": {},
                    "CombineText-lwhhK": {},
                    "Prompt-UbjFI": {
                        "platform": platform,
                        "post_type": post_type
                    },
                    "TextInput-zxxDX": {
                        "input_value": platform
                    },
                    "TextInput-vYC1a": {
                        "input_value": post_type
                    }
                }
            }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': os.getenv("LANGFLOW_AUTH_TOKEN")
            }

            api_url = os.getenv("LANGFLOW_REPORT_URL")
            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 200:
                st.write("Request was successful!")
                json_data = response.json()
                st.write(json_data["outputs"][0]["outputs"][0]["results"]["message"]["text"])
            else:
                st.write(f"Request failed with status code {response.status_code}")
                st.write(response.text)
    else:
        st.write("Please enter a message to send.")
