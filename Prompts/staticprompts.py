from langchain_openai import    ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
model=ChatOpenAI(model="gpt-4")
st.header("Reaserch Tool")
user_input=st.text_input("enter the Prompt")
if st.button("Summarize"):
    result=model.invoke(user_input)
    st.write(result.content)
