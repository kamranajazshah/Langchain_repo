from langchain_openai import    ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
model=ChatOpenAI(model="gpt-4")
st.header("Reaserch Tool")
paper_input=st.selectbox("Select Reaserch Paper",["Attention all you need","BERT:Bidirectional Encoder Representation from Transformer","Diffusion"])
style_input=st.selectbox("Select the Expression style",["Beginner-Friendly","Technical","Mathematical"])
length_input=st.selectbox("Select the output length",["Minimum 3 lines","Intermidiate 5 Lines","Maximum 10 Lines"])
templete=load_prompt("Prompt.json")
prompt=templete.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})
if st.button("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)
