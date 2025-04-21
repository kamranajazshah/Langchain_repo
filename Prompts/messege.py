#Messages
""" it is the one the important topic in our langchain which help in to differentiate between ai_message,human_message and ai message.
it help you to store the messages and provide the ai the information about previous talk which help them to know the context and can work more on it 

"""
#to import we write
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()
messages=[SystemMessage(content="you are an chat assistant"),
        HumanMessage(content="what is the  captail of india")
        ]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)