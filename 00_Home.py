import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="PK - Potter - Social Media Engagement Analyser", page_icon="📊", layout="centered", menu_items={'Get Help': 'https://google.com'})
st.set_option('client.toolbarMode', "Minimal")

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

st.markdown("<h3 style='text-align: center;'>Meet Our Developers</h3>", unsafe_allow_html=True)

card_style = """
<style>
.card {
    text-align: center;
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.card img {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin-bottom: 15px;
}

.card h3 {
    margin: 10px 0 5px;
    font-size: 20px;
    color: #333333;
}

.card p {
    margin: 0;
    font-size: 16px;
    color: #666666;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

dev1_name = "Kirubhaharan B"
dev1_degree = "MSc Data Science and Analytics"
linkedIn_1 = "https://www.linkedin.com/in/kirubhaharanb/"
 
dev2_name = "Prashanth Rao"
dev2_degree = "MSc Data Science and Analytics"
linkedIn_2 = "https://www.linkedin.com/in/prashanth-raghavendra-rao/"

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="card">
            <h3>{dev1_name}</h3>
            <p>{dev1_degree}</p>
            <a href={linkedIn_1}>Let's Connect</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="card">
            <h3>{dev2_name}</h3>
            <p>{dev2_degree}</p>
            <a href={linkedIn_2}>Let's Connect</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
