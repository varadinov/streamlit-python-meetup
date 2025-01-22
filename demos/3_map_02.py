from functools import partial
import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(layout='wide')

def get_color(population: int, min_population: int, max_population: int):
    """ Scale population between 0 (green) and 1 (red) """
    scale = (population - min_population) / (max_population - min_population)
    red = int(scale * 255)  # More population = more red
    green =  int((1 - scale) * 255)  # Less population = more green
    return [red, green, 0, 140]

@st.cache_data
def load_data():
    return pd.read_csv("data/full_population.csv")

df = load_data()

# Add filters
initial_max_population = df["Population"].max()
initial_min_population = df["Population"].min()
year = st.selectbox("Year", df['Year'].unique(), key="year")
admin_cities = st.multiselect("Admin City", df['AdminCity'].unique(), default=df['AdminCity'].unique(), key="admin-city-select")
selected_min, selected_max = st.slider("Population Min", initial_min_population, initial_max_population, (initial_min_population, initial_max_population), key="min-max-slider22")
df = df.query(f'Year == @year and AdminCity in @admin_cities and Population > @selected_min and Population < @selected_max')

# Apply color
df["color"] = df["Population"].apply(partial(get_color, min_population=df["Population"].min(), max_population=df["Population"].max()))

st.title("Bulgarian Cities Map")
st.pydeck_chart(
    pdk.Deck(
        map_style='light',
        layers=[
            pdk.Layer(
                "ColumnLayer",
                data=df,
                get_position="[Longitude, Latitude]",
                get_elevation="Population",
                get_fill_color='color',
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
            "html": """<b>City:</b> {City}<br />
                       <b>Population:</b> {Population}<br />
                       <b>Male Population:</b> {Male}<br />
                       <b>Female Population:</b> {Female}<br />
                       <b>Year:</b> {Year}<br />
                       """,
            "style": {"backgroundColor": "steelblue", "color": "white"},
        }
    )
)