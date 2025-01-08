import streamlit as st
import pandas as pd
from plot_functions.EngagementRateOverTime import EngagementRateOverTime
from plot_functions.EngagementBreakdownByPostType import EngagementBreakdownByPostType
from plot_functions.PlatformPerformanceComparison import PlatformPerformanceComparison
from plot_functions.PostEngagementDistribution import PostEngagementDistribution
from plot_functions.AudienceGenderDistribution import AudienceGenderDistribution
from plot_functions.AudienceAgeDistribution import AudienceAgeDistribution
from plot_functions.AudienceLocationDistribution import AudienceLocationDistribution
from plot_functions.TopPerformingPosts import TopPerformingPosts
from plot_functions.PostFrequencyAnalysis import PostFrequencyAnalysis
from plot_functions.ImpressionsToReachRatioAnalysis import ImpressionsToReachRatioAnalysis
from astrapy import DataAPIClient
import pandas as pd
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

client = DataAPIClient(os.getenv('ASTRA_DB_TOKEN'))
db = client.get_database_by_api_endpoint(st.secrets["ASTRA_DB_ENDPOINT"])

desired_collection = st.secrets["ASTRA_DB_COLLECTION_NAME"]

collection = db.get_collection(desired_collection)
documents = collection.find({})

if documents:
    df = pd.DataFrame(documents)
    st.session_state.df = df
else:
    st.write(f"No data found in collection '{desired_collection}'.")

st.title("Social Media Engagement Analytics Dashboard")

plot_options = [
    "Engagement Rate Over Time",
    "Engagement Breakdown by Post Type",
    "Platform Performance Comparison",
    "Post Engagement Distribution",
    "Audience Gender Distribution",
    "Audience Age Distribution",
    "Audience Location Distribution",
    "Top Performing Posts",
    "Post Frequency Analysis",
    "Impressions-to-Reach Ratio Analysis"
]

selected_plot = st.sidebar.radio("Select Plot to Display", plot_options)

if selected_plot in ["Engagement Rate Over Time", "Post Frequency Analysis"]:
    time_granularity = st.sidebar.radio("Select Time Granularity", ["Daily", "Monthly", "Yearly"])
else:
    time_granularity = None

if selected_plot == "Engagement Rate Over Time":
    if time_granularity:
        plotter = EngagementRateOverTime(df, time_granularity)
        plotter.plot()
    else:
        st.warning("Please select a time granularity for this plot.")
        
elif selected_plot == "Engagement Breakdown by Post Type":
    plotter = EngagementBreakdownByPostType(df)
    plotter.plot()
    
elif selected_plot == "Platform Performance Comparison":
    plotter = PlatformPerformanceComparison(df)
    plotter.plot()
    
elif selected_plot == "Post Engagement Distribution":
    plotter = PostEngagementDistribution(df)
    plotter.plot()
    
elif selected_plot == "Audience Gender Distribution":
    plotter = AudienceGenderDistribution(df)
    plotter.plot()
    
elif selected_plot == "Audience Age Distribution":
    plotter = AudienceAgeDistribution(df)
    plotter.plot()
    
elif selected_plot == "Audience Location Distribution":
    plotter = AudienceLocationDistribution(df)
    plotter.plot()
    
elif selected_plot == "Top Performing Posts":
    plotter = TopPerformingPosts(df)
    plotter.plot()
    
elif selected_plot == "Post Frequency Analysis":
    if time_granularity:
        plotter = PostFrequencyAnalysis(df, time_granularity)
        plotter.plot()
    else:
        st.warning("Please select a time granularity for this plot.")
        
elif selected_plot == "Impressions-to-Reach Ratio Analysis":
    plotter = ImpressionsToReachRatioAnalysis(df)
    plotter.plot()
