import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

st.title("✉️ AI Email Writer")

email_type = st.selectbox(
    "Email Type",
    [
        "Sales Email",
        "Client Follow Up",
        "Marketing Email",
        "Professional Reply"
    ]
)

prompt = st.text_area("Enter Email Requirement")

if st.button("Generate Email"):

    full_prompt = f"Write a professional {email_type}. {prompt}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    output = response.choices[0].message.content

    st.subheader("Generated Email")

    st.write(output)
