import streamlit as st
import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Background style
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #e5e5f7;
opacity: 0.8;
background-image:  radial-gradient(#444cf7 1.1px, transparent 1.1px), radial-gradient(#444cf7 1.1px, #e5e5f7 1.1px);
background-size: 44px 44px;
background-position: 0 0,22px 22px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to load Lottie animation
def load_lottie_local(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading Lottie file: {e}")
        return None

# Header
st.header("Let us know about your platform and post type for insights!")

# Dropdown for platform selection (sorted alphabetically)
platform = st.selectbox(
    "What platform are you posting?",
    ["Instagram", "Facebook", "LinkedIn", "Twitter"]
)

# Dropdown for post type selection
post_type = st.selectbox(
    "What is the type of your post?",
    ["Image", "Video", "Carousel"]
)

# Button to submit form
if st.button('Submit'):
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
                        "platform": platform,  # Use the selected platform here
                        "post_type": post_type  # Use the selected post type here
                    },
                    "TextInput-zxxDX": {
                        "input_value": platform  # Use the selected platform here
                    },
                    "TextInput-vYC1a": {
                        "input_value": post_type  # Use the selected post type here
                    }
                }
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': os.getenv("LANGFLOW_AUTH_TOKEN")
            }

            # API URL from environment variable
            api_url = os.getenv("LANGFLOW_REPORT_URL")
            response = requests.post(api_url, json=payload, headers=headers)

            # Handling response
            if response.status_code == 200:
                st.write("Request was successful!")
                json_data = response.json()
                st.write(json_data["outputs"][0]["outputs"][0]["results"]["message"]["text"])
            else:
                st.write(f"Request failed with status code {response.status_code}")
                st.write(response.text)
    else:
        st.write("Please select both platform and post type to proceed.")
