import streamlit as st
import requests
import time
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

def load_css():
    with open("styles/chatbot_styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def initialize_session_state():
    if "messages" not in st.session_state or st.sidebar.button("Clear conversation history"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


def send_to_langflow(message):
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {
            "File-p0FEt": {},
            "SplitText-lbYFU": {},
            "AstraDB-uY8GQ": {"number_of_results": 200},
            "TextInput-fidnT": {},
            "ParseData-ORbJR": {},
            "ChatOutput-SFU6h": {},
            "Agent-SgCdj": {},
            "ChatInput-0en8b": {},
            "CombineText-JQhuo": {},
            "CombineText-qPiG8": {},
        },
    }
    api_url = os.getenv("LANGFLOW_CHATBOT_URL")
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv("LANGFLOW_AUTH_TOKEN"),
    }

    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        return json_data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
    else:
        return f"Error: {response.status_code}"

load_css()
initialize_session_state()

st.header("Chat with your data")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-row row-reverse">
                <div class="chat-bubble human-bubble">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="chat-row">
                <div class="chat-bubble ai-bubble">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


user_question = st.chat_input("Ask a question. Let me assist you.")
if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    st.markdown(
        f"""
        <div class="chat-row row-reverse">
            <div class="chat-bubble human-bubble">{user_question}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.spinner("Generating response... Please wait!"):
        response = send_to_langflow(user_question)
        time.sleep(2)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(
            f"""
            <div class="chat-row">
                <div class="chat-bubble ai-bubble">{response}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
