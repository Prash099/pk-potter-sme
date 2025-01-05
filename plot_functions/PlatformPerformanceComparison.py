import pandas as pd
import plotly.express as px
import streamlit as st

class PlatformPerformanceComparison:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if {'platform', 'impressions', 'reach', 'engagement_rate'}.issubset(self.df.columns):
            platform_metrics = self.df.groupby('platform')[['impressions', 'reach', 'engagement_rate']].mean().reset_index()
            fig = px.bar(platform_metrics, x="platform", y=['impressions', 'reach', 'engagement_rate'], 
                         barmode='group', title="Platform Performance Comparison")
            st.plotly_chart(fig)
        else:
            st.warning("Required columns are missing for this plot.")
