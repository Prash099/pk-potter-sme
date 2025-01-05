import pandas as pd
import plotly.express as px
import streamlit as st

class EngagementBreakdownByPostType:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if {'likes', 'comments', 'shares', 'post_type'}.issubset(self.df.columns):
            engagement_cols = ['likes', 'comments', 'shares']
            engagement_by_post_type = self.df.groupby('post_type')[engagement_cols].sum().reset_index()
            fig = px.bar(engagement_by_post_type, x="post_type", y=engagement_cols, 
                         barmode='group', title="Engagement Breakdown by Post Type")
            st.plotly_chart(fig)
        else:
            st.warning("Required columns are missing for this plot.")
