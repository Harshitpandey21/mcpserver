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
