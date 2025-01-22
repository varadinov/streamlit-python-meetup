import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generate random data
def generate_random_data(num_points=150):
    np.random.seed(42)
    data = {
        "x": np.random.uniform(1.0, 10.0, num_points),
        "y": np.random.uniform(1.0, 10.0, num_points),
        "category": np.random.choice(["Category A", "Category B", "Category C"], num_points),
        "size": np.random.uniform(10, 100, num_points),
        "hover_info": np.random.uniform(1.0, 5.0, num_points),
    }
    return pd.DataFrame(data)

# Create a random dataset
df = generate_random_data()

# Create the scatter plot with Plotly
fig = px.scatter(
    df,
    x="x",
    y="y",
    color="category",
    size="size",
    hover_data=["hover_info"],
    title="Randomly Generated Data Scatter Plot"
)

# Render the chart with Streamlit and enable selection
st.write("### Select points by drawing a rectangle on the plot")
event = st.plotly_chart(fig, key="random-data", on_select="rerun")

# Display selection data (if available)
if event and hasattr(event, "selection"):
    st.write("### Selected Points")
    st.write(event.selection)
else:
    st.write("Use the lasso or rectangle tool on the chart to select points.")