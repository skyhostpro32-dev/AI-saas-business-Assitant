import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["sk-...oaEA"]
)

st.title("🤖 Customer Support Chatbot")

user_input = st.text_input("Ask Your Question")

if st.button("Send"):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful business support assistant"
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    reply = response.choices[0].message.content

    st.success(reply)
