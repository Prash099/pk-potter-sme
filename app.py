import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_css():
    with open("home.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_welcome_animation():
    url = "https://assets2.lottiefiles.com/packages/lf20_f5lq8vkp.json"  
    animation = load_lottie_url(url)
    if animation:
        st_lottie(animation, speed=1, width=700, height=400, key="welcome_animation")

st.set_page_config(page_title="Social Media Analyzer", page_icon="📊", layout="centered")

load_css()

st.title("Welcome to the Social Media Analyzer")
st.write("Analyze and gain insights from your social media data easily using AI-powered technologies!")

load_welcome_animation()

st.header("Key Features:")
st.write("📊 **Data Analysis:** Analyze social media data from multiple platforms.")
st.write("🤖 **AI Insights:** Leverage AI to extract meaningful insights from raw data.")
st.write("⚡ **Real-time Data:** Get real-time updates and analytics.")
st.write("💬 **User-Friendly Interface:** Easy-to-use interface for quick and efficient results.")

st.markdown("""
    <div class="footer">
        <p>Powered by:</p>
        <div class="footer-icons">
            <img src="static/Datastax_logo.png" width="50" height="50" alt="Datastax">
            <img src="static/langflow.svg" width="50" height="50" alt="Langflow">
            <img src="static/aws.svg" width="50" height="50" alt="AWS">
            <img src="static/streamlit.svg" width="50" height="50" alt="Streamlit">
        </div>
    </div>
""", unsafe_allow_html=True)




