import pandas as pd
import plotly.express as px
import streamlit as st

class AudienceGenderDistribution:
    def __init__(self, df):
        self.df = df
    
    def plot(self):
        if 'audience_gender' in self.df:
            gender_data = self.df.groupby('audience_gender').size().reset_index(name='count')
            fig = px.pie(gender_data, values='count', names='audience_gender', title="Audience Gender Distribution")
            st.plotly_chart(fig)
        else:
            st.warning("Required column is missing for this plot.")
