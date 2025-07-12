
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq

#from groq import Groq
import os

load_dotenv()

grog_api_key = os.getenv("GROG_API_KEY")

llm = ChatGroq(api_key = grog_api_key, model_name= "llama-3.1-8b-instant" )

if __name__ == "__main__":
    response = llm.invoke("What are the main ingredients in pani puri")
    print(response.content)
