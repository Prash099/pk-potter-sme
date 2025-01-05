import streamlit as st
from streamlit_lottie import st_lottie
import json

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

def load_lottie_local(file_path: str):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading Lottie animation from file: {e}")
        return None

def load_css():
    with open("styles/home.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_welcome_animation():
    local_file_path = "lottie_animations/animation_2.json"  
    animation = load_lottie_local(local_file_path)
    if animation:
        col1, col2 = st.columns([1, 2]) 

        with col1:
            st.write("")
            st_lottie(animation, speed=1, width=220, height=200, key="welcome_animation")

        with col2:
            st.title("Welcome to the Social Media Analyzer")
            st.write("Analyze and gain insights from your social media data easily using AI-powered technologies!")

load_css()

load_welcome_animation()

st.header("Key Features:")
st.write("📊 **Data Analysis:** Analyze social media data from multiple platforms.")
st.write("🤖 **AI Insights:** Leverage AI to extract meaningful insights from raw data.")
st.write("⚡ **Real-time Data:** Get real-time updates and analytics.")
st.write("💬 **User-Friendly Interface:** Easy-to-use interface for quick and efficient results.")

st.write("")  
st.write("")  

st.markdown("<h3 style='text-align: center; color: #333;'>Powered by:</h3>", unsafe_allow_html=True)

st.markdown("""
    <div style="width: 100%; overflow: hidden;">
        <div style="display: flex; animation: marquee 15s linear infinite;">
            <div style="padding: 0 20px;">
                <h3>Datastax</h3>
            </div>
            <div style="padding: 0 20px;">
                <h3>Langflow</h3>
            </div>
            <div style="padding: 0 20px;">
                <h3>AWS</h3>
            </div>
            <div style="padding: 0 20px;">
                <h3>Streamlit</h3>
            </div>
        </div>
    </div>
    <style>
        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
    </style>
""", unsafe_allow_html=True)
