import streamlit as st
from fpdf import FPDF

st.title("🧾 AI Invoice Generator")

customer_name = st.text_input("Customer Name")
product_name = st.text_input("Product Name")
price = st.number_input("Price", min_value=0.0)
quantity = st.number_input("Quantity", min_value=1)


total = price * quantity

st.subheader(f"Total Amount: ₹{total}")

if st.button("Generate Invoice PDF"):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)

    pdf.cell(200, 10, txt="Invoice", ln=True)
    pdf.cell(200, 10, txt=f"Customer: {customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Product: {product_name}", ln=True)
    pdf.cell(200, 10, txt=f"Total: ₹{total}", ln=True)

    pdf.output("invoice.pdf")

    with open("invoice.pdf", "rb") as file:
        st.download_button(
            label="Download Invoice",
            data=file,
            file_name="invoice.pdf",
            mime="application/pdf"
        )
