from dotenv import load_dotenv, find_dotenv
load_dotenv('.venv')

import streamlit as st
from langchain_openai import ChatOpenAI

chat_llm = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo", max_tokens=100)

def generate_response(user_input):
    return chat_llm.predict(user_input)

# Streamlit app layout
def main():
    st.set_page_config(page_title="AI Agent", page_icon=":robot_face:")

    st.title("AI Agent")

    st.write("Welcome to AI Agent!")
    st.write("Start a conversation by typing in the box below:")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        response = generate_response(user_input)
        st.text_area("Bot:", response)

if __name__ == "__main__":
    main()
