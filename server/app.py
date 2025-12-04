import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

CONFIG_FILE = "server/weather.json"
@st.cache_resource
def init_agent():
    client = MCPClient.from_config_file(CONFIG_FILE)
    llm = ChatOpenAI(model="gpt-4o")
    agent = MCPAgent(llm=llm, client=client, max_steps=15, memory_enabled=True)
    return agent, client

agent, client = init_agent()

st.title(" MCP Weather Chat")
st.write("Talk to the weather MCP agent using your custom tool.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    role, msg = m
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

user_input = st.chat_input("Ask something...")
if user_input:
    st.session_state.messages.append(("user", user_input))
    st.chat_message("user").write(user_input)

    async def get_reply():
        try:
            reply = await agent.run(user_input)
            return reply
        except Exception as e:
            return f"Error: {e}"

    reply = asyncio.run(get_reply())
    st.session_state.messages.append(("assistant", reply))

    st.chat_message("assistant").write(reply)

if st.button(" Clear Memory"):
    agent.clear_conversation_history()
    st.session_state.messages = []
    st.success("Memory cleared")

async def close_sessions():
    if client and client.sessions:
        await client.close_all_sessions()

if st.button("Shutdown MCP sessions"):
    asyncio.run(close_sessions())
    st.success("MCP sessions closed")

