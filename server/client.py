import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
async def run_memory_chat():
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    config_file = "server/weather.json"
    print("Initializing chat...")

    client = MCPClient.from_config_file(config_file)
    llm=ChatOpenAI(model="gpt-4o")
    agent=MCPAgent(llm=llm,client=client,max_steps=15,memory_enabled=True)

    print("\nAgent initialized. You can start chatting now!")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("Type 'clear' to clear the memory.")
    
    try:
        while True:
            user_input=input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("\nexited successfully")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("\nMemory cleared.")
                continue

            try:
                response=await agent.run(user_input)
                print("\nAssistant: ", response)
            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.sessions:
          await client.close_all_sessions()
          print("Chat session ended.")

if __name__ == "__main__":
    asyncio.run(run_memory_chat())