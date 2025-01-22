import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.title("Streamlit assistant bot")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ['OPENAI_API_KEY'],
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "mistralai/mistral-7b-instruct:free"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are an assistant that only discusses streamlit topics. Do not answer questions outside this scope."}]

for message in st.session_state.messages:
    if message["role"] != 'system':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})