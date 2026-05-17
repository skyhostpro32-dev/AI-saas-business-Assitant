import streamlit as st

# ---------------- PAGE TITLE ----------------

st.title("✉️ AI Email Writer")

st.write("Generate professional business emails instantly")

# ---------------- EMAIL TYPE ----------------

email_type = st.selectbox(
    "Select Email Type",
    [
        "Sales Email",
        "Client Follow Up",
        "Marketing Email",
        "Professional Reply"
    ]
)

# ---------------- USER INPUT ----------------

client_name = st.text_input("Client Name")

company_name = st.text_input("Company Name")

purpose = st.text_area("Enter Email Requirement")

# ---------------- GENERATE EMAIL ----------------

if st.button("Generate Email"):

    if email_type == "Sales Email":

        output = f"""
Subject: Helping {company_name} Grow Faster

Dear {client_name},

I hope you are doing well.

I wanted to reach out regarding {purpose}. Our solutions can help improve efficiency, productivity, and business growth.

I would love to schedule a quick discussion to explore how we can work together.

Looking forward to your response.

Best Regards,
Your Name
"""

    elif email_type == "Client Follow Up":

        output = f"""
Subject: Follow Up Regarding Our Discussion

Dear {client_name},

I hope you are doing well.

I am following up regarding {purpose}. Please let me know if you need any additional information from my side.

Looking forward to hearing from you.

Best Regards,
Your Name
"""

    elif email_type == "Marketing Email":

        output = f"""
Subject: Special Update for {company_name}

Dear {client_name},

We are excited to share updates regarding {purpose}.

Our latest solutions are designed to improve business performance and simplify workflows.

Feel free to contact us for more details.

Best Regards,
Your Name
"""

    else:

        output = f"""
Subject: Professional Response

Dear {client_name},

Thank you for your message regarding {purpose}.

I appreciate your time and will get back to you with the required information as soon as possible.

Best Regards,
Your Name
"""

    # ---------------- OUTPUT ----------------

    st.subheader("📧 Generated Email")

    st.text_area(
        "Generated Email",
        output,
        height=300
    )
