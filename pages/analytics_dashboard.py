import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Sales Analytics Dashboard")

sales_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [20000, 35000, 42000, 38000, 50000]
})

fig = px.line(
    sales_data,
    x="Month",
    y="Revenue",
    title="Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)
