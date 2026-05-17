import streamlit as st
import pandas as pd

st.title("📁 Excel Automation Tool")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx", "csv"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")

    st.dataframe(df)

    st.subheader("Basic) 
