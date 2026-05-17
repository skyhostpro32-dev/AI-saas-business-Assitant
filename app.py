import streamlit as st

st.set_page_config(
    page_title="AI SaaS Business Assistant",
    layout="wide"
)

# ---------------- CSS ----------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🚀 AI SaaS Business Assistant")

st.write("Business Automation Platform using AI")
# ---------------- DASHBOARD CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Revenue", "₹1,25,000")

with col2:
    st.metric("Invoices", "120")

with col3:
    st.metric("Customers", "58")

with col4:
    st.metric("AI Insights", "24")
# ---------------- FEATURES ----------------

st.subheader("✨ Platform Features")

feature_col1, feature_col2, feature_col3 = st.columns(3)

with feature_col1:
    st.success("AI Invoice Generator")
    st.success("AI Email Writer")

with feature_col2:
   st.success("Customer Chatbot")
   st.success("Excel Automation")

with feature_col3:
    st.success("Analytics Dashboard")
    st.success("AI Reports")
