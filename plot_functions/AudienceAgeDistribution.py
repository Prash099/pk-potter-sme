import pandas as pd
import plotly.express as px
import streamlit as st

class AudienceAgeDistribution:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if 'audience_age' in self.df:
            age_data = self.df.groupby('audience_age').size().reset_index(name='count')
            fig = px.bar(age_data, x="audience_age", y="count", 
                         title="Audience Age Distribution", labels={"count": "Count", "audience_age": "Age Group"})
            st.plotly_chart(fig)
        else:
            st.warning("Required column is missing for this plot.")
