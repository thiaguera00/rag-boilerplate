from langchain_openai import ChatOpenAI
from ..utils.config import OPENAI_API_KEY

def get_llm(model: str = "gpt-4"):
    return ChatOpenAI(model=model, openai_api_key=OPENAI_API_KEY)
