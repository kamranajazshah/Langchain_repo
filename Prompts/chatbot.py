from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
model=ChatOpenAI()
messages=[SystemMessage(content="YOU ARE ANY CHAT ASSISTANT")
]
st.header("Simple AI ChatBot")

while True:
    user_input=st.text_input("You:")
    messages.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    st.write("A.I",result.content)
