from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
documents=["i am kamran",
           "tabbeb is here",
           "hello"

]
model=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
result=model.embed_documents(documents)
print(result[0])
