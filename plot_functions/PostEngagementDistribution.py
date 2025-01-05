import pandas as pd
import plotly.express as px
import streamlit as st

class PostEngagementDistribution:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if {'likes', 'comments', 'shares', 'post_type', 'platform'}.issubset(self.df.columns):
            engagement_distribution = self.df.groupby(['post_type', 'platform'])[['likes', 'comments', 'shares']].sum().reset_index()
            fig = px.bar(engagement_distribution, x="post_type", y=["likes", "comments", "shares"], 
                         color="platform", title="Post Engagement Type Distribution", barmode="stack")
            st.plotly_chart(fig)
        else:
            st.warning("Required columns are missing for this plot.")
