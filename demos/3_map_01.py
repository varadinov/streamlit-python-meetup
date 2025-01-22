from functools import partial
import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(layout='wide')

df = pd.read_csv("data/full_population.csv")
df = df.query(f'Year == 2023')

st.title("Bulgarian Cities Map")
st.pydeck_chart(
    pdk.Deck(
        map_style='light',
        height=1500,
        layers=[
            pdk.Layer(
                "ColumnLayer",
                data=df,
                get_position="[Longitude, Latitude]",
                get_elevation="Population",
                get_fill_color=[20,200,20, 140],
                radius=2000,
                elevation_scale=0.05,
                elevation_range=[0, 100],
                pickable=True,
                extruded=True,
                auto_highlight=True
            )
        ],
        initial_view_state=pdk.ViewState(
            latitude=df["Latitude"].mean(),
            longitude=df["Longitude"].mean(),
            controller = True,
            zoom=7,
            pitch=50,
        ),
        tooltip = {
            "html": "<b>Population:</b> {Population}<br />",
            "style": {"backgroundColor": "steelblue", "color": "white"},
        }
    )
)