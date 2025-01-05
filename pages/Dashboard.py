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

# Initialize Astra DB Client
client = DataAPIClient("AstraCS:yneBpwTqwQfWiOpctxkhmlyK:ad7734828392ef925f732b502d37a165877cd8d7bc518480e89e04c82b2594c2")
db = client.get_database_by_api_endpoint(
    "https://76715bec-7a1f-409d-bc03-c5fdfdc0ceb8-us-east-2.apps.astra.datastax.com"
)

# Desired collection in Astra DB
desired_collection = 'sm_engagement_data'

# Fetch data from Astra DB collection
collection = db.get_collection(desired_collection)
documents = collection.find({})

if documents:
    # Convert documents to a pandas DataFrame
    df = pd.DataFrame(documents)
    st.session_state.df = df  # Store DataFrame in session state
else:
    st.write(f"No data found in collection '{desired_collection}'.")

# Dashboard title
st.title("Social Media Engagement Analytics Dashboard")

# Plot options
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

# Sidebar plot selection
selected_plot = st.sidebar.radio("Select Plot to Display", plot_options)

# Time granularity selection for time-based plots
if selected_plot in ["Engagement Rate Over Time", "Post Frequency Analysis"]:
    time_granularity = st.sidebar.radio("Select Time Granularity", ["Daily", "Monthly", "Yearly"])
else:
    time_granularity = None

# Plotting logic based on selected plot
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
