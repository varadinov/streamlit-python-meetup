import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Chart Demo")
st.subheader("Dynamic Charts with Random Data")

# Generate random data
st.sidebar.header("Chart Configuration")
rows = st.sidebar.slider("Number of Rows", 10, 100, 50)
cols = st.sidebar.slider("Number of Columns", 1, 5, 3)

data = pd.DataFrame(
    np.random.randn(rows, cols),
    columns=[f"Column {i+1}" for i in range(cols)]
)

# Display table and charts
st.write("### Random Data Table")
st.dataframe(data)

st.write("### Line Chart")
st.line_chart(data)

st.write("### Bar Chart")
st.bar_chart(data)

st.write("### Area Chart")
st.area_chart(data)

if st.checkbox("Show Data Summary"):
    st.write("### Data Summary")
    st.write(data.describe())