import pandas as pd
import plotly.express as px
import streamlit as st

class TopPerformingPosts:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if {'post_content', 'engagement_rate', 'platform'}.issubset(self.df.columns):
            top_posts = self.df.sort_values(by='engagement_rate', ascending=False).head(10)
            fig = px.bar(top_posts, x="post_content", y="engagement_rate", color="platform", 
                         title="Top Performing Posts (Engagement Rate)")
            st.plotly_chart(fig)
        else:
            st.warning("Required columns are missing for this plot.")
