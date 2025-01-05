import pandas as pd
import plotly.express as px
import streamlit as st

class EngagementRateOverTime:
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
        if 'time_period' in self.df and 'engagement_rate' in self.df:
            aggregated_data = self.df.groupby(['time_period', 'platform'])['engagement_rate'].mean().reset_index()
            fig = px.line(
                aggregated_data,
                x="time_period",
                y="engagement_rate",
                color="platform",
                title=f"Engagement Rate Over Time ({self.time_granularity})",
                labels={"engagement_rate": "Avg. Engagement Rate", "time_period": "Time Period"}
            )
            fig.update_traces(mode="lines+markers")
            st.plotly_chart(fig)
        else:
            st.warning("Required columns are missing for this plot.")
