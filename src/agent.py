from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os

from .tools import get_column_stats


load_dotenv()

model = ChatOpenAI(temperature=0, model='gpt-4o')

def create_agent(df):
    tools=[
        Tool(
            name="Get Column Stats",
            function=lambda col:get_column_stats(df, col),
            description="Get basic statistics of a column."
        ),
        #Tool()
    ]


    agent=initialize_agent(
        tools=tools,
        llm=model,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent