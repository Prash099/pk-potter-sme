import pandas as pd
import plotly.express as px
import streamlit as st

class PostFrequencyAnalysis:
    def __init__(self, df, time_granularity):
        self.df = df
        self.time_granularity = time_granularity
    
    def aggregate_data(self):
        if 'post_timestamp' not in self.df:
            st.warning("Timestamp column is missing.")
            return pd.DataFrame()
        self.df['date'] = pd.to_datetime(self.df['post_timestamp'])
        if self.time_granularity == "Daily":
            self.df['time_period'] = self.df['date'].dt.date
        elif self.time_granularity == "Monthly":
            self.df['time_period'] = self.df['date'].dt.to_period('M').dt.to_timestamp()
        elif self.time_granularity == "Yearly":
            self.df['time_period'] = self.df['date'].dt.to_period('Y').dt.to_timestamp()
        return self.df
    
    def plot(self):
        self.df = self.aggregate_data()
        if 'time_period' in self.df:
            post_frequency = self.df.groupby('time_period').size().reset_index(name='post_count')
            fig = px.line(post_frequency, x="time_period", y="post_count", 
                          title=f"Post Frequency Over Time ({self.time_granularity})")
            st.plotly_chart(fig)
        else:
            st.warning("Required column is missing for this plot.")
