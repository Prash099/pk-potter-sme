import streamlit as st
import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="PK - Potter - Social Media Engagement Analyser", page_icon="📊", layout="centered",menu_items={'Get Help': 'https://google.com'})
st.set_option('client.toolbarMode',"Minimal")

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

def load_lottie_local(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading Lottie file: {e}")
        return None

st.header("Let us know about your platform and post type for insights!")

platform = st.selectbox(
    "What platform are you posting?",
    ["Instagram", "Facebook", "LinkedIn", "Twitter"]
)

post_type = st.selectbox(
    "What is the type of your post?",
    ["Image", "Video", "Carousel"]
)

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
                'Authorization': st.secrets["LANGFLOW_AUTH_TOKEN"]
            }

            api_url = st.secrets["LANGFLOW_REPORT_URL"]
            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 200:
                st.write("Request was successful!")
                json_data = response.json()
                st.write(json_data["outputs"][0]["outputs"][0]["results"]["message"]["text"])
            else:
                st.write(f"Request failed with status code {response.status_code}")
                st.write(response.text)
    else:
        st.write("Please select both platform and post type to proceed.")
