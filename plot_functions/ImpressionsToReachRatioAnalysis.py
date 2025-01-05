import pandas as pd
import plotly.express as px
import streamlit as st

class ImpressionsToReachRatioAnalysis:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if {'platform', 'impressions', 'reach'}.issubset(self.df.columns):
            self.df['impressions_to_reach_ratio'] = self.df['impressions'] / self.df['reach']
            platform_ratios = self.df.groupby('platform')['impressions_to_reach_ratio'].mean().reset_index()
            fig = px.bar(platform_ratios, x="platform", y="impressions_to_reach_ratio", 
                         title="Average Impressions-to-Reach Ratio by Platform")
            st.plotly_chart(fig)
        else:
            st.warning("Required columns are missing for this plot.")
