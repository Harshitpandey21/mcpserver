MCP Weather Server + Streamlit Chat Client

This repository provides a working implementation of an MCP Server (Model Context Protocol) that exposes a custom tool to fetch live U.S. weather alerts from the National Weather Service (NWS).
The MCP server can be accessed through:

* ✔ Local Python IDE (via MCPAgent)

* ✔ Streamlit Chat UI (visual interface)

* ✔ Any MCP-compatible LLM client

# Project Structure
```
mcpserver/
├── server/
│   ├── weather.py          # MCP server (FastMCP + NWS tool)
│   ├── weather.json        # MCP config file
│   └── app.py              # Streamlit chat UI
│   └── client.py           # Local IDE chat server
├── requirements.txt
└── README.md

```
# Installation

1. Clone the repository
  ```
  git clone https://github.com/Harshitpandey21/mcpserver.git
  cd mcpserver
  ```

2. Install dependencies
 ```
  pip install -r requirements.txt
  ```

4. Set OpenAI API KEY
 ```
 OPENAI_API_KEY = "YOUR_KEY_HERE"
 ```
   
# Running the MCP Server Locally
  The MCP server is defined in weather.py.
  
  To start the server:
  ```
  uv run mcp dev server/weather.py
  ```
# Using from a Local IDE / Terminal Client
  To start the server:
  ```
  uv run server/client.py
  ```
# Running the Streamlit Chat UI
  To start the server:
  ```
  streamlit run server/app.py
  ```
# requirements.txt
```
langchain-openai
langchain-groq
streamlit
"mcp[cli]"
mcp-use
```

