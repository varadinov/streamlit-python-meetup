import streamlit as st
import pandas as pd

# File path for the CSV
csv_file = "data/edit_data_from_data.csv"

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

df = load_data(csv_file)

df["Position"] = (
    df["Position"].astype("category").cat.set_categories(['Developer', 'DevOps', 'QA', 'Manager', 'Director'])
)

st.title("Editable DataFrame")
edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

if st.button("Save Data"):
    save_data(edited_df, csv_file)
    st.success("Changes saved to CSV!")
