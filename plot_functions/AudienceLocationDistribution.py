import pandas as pd
import plotly.express as px
import streamlit as st

class AudienceLocationDistribution:
    def __init__(self, df):
        self.df = df

    def plot(self):
        if 'latitude' not in self.df.columns or 'longitude' not in self.df.columns:
            st.warning("Latitude and longitude columns are missing in the data.")
            return
        
        geo_df = self.df.dropna(subset=['latitude', 'longitude'])

        if geo_df.empty:
            st.warning("No valid locations were found to plot on the map.")
            return

        fig = px.scatter_geo(geo_df, lat='latitude', lon='longitude', text='audience_location',
                             title="Audience Location Distribution",
                             labels={'audience_location': 'Location'},
                             projection="natural earth", 
                             template="plotly", 
                             hover_name="audience_location")
        
        st.plotly_chart(fig)
