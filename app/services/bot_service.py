from ..infrastructure.rag_pipeline import build_rag_pipeline
from ..infrastructure.llm_client import get_llm
from .bot_tools import schedule_appointment
from ..utils.response_formatter import response_formatter
from langchain.agents import initialize_agent, AgentType

rag_chain = build_rag_pipeline("base.txt")

llm = get_llm()

tools = [schedule_appointment]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def response_llm(question: str) -> str:
    if "funciona" in question or "horario" in question:
        ai_response = rag_chain.invoke(question)
    else: 
        ai_response = agent.invoke({"input":question})

    return response_formatter(ai_response)
