from langchain.chat_models import init_chat_model
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

from dotenv import load_dotenv
from load import load_data

load_dotenv()

def agent_start():
    db=load_data(r'data\march_detalized.xlsx',"performance","detalized")
    llm = init_chat_model('gpt-4o-mini', model_provider='openai')

    toolkit = SQLDatabaseToolkit(db=db, llm=llm, top_k=None)
    agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, agent_type="openai-tools", verbose=False, return_intermediate_steps=True)

    return agent_executor