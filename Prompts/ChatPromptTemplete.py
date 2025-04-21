from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
templete=ChatPromptTemplate([(
    "system","you are the {domain} expert"
),
("human","what is {balltype}")])
prompt=templete.invoke({"domain":"cricket","balltype":"Doosra"})
print(prompt)
