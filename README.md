MCP Weather Server + Streamlit Chat Client

This repository provides a working implementation of an MCP Server (Model Context Protocol) that exposes a custom tool to fetch live U.S. weather alerts from the National Weather Service (NWS).
The MCP server can be accessed through:

* ✔ Local Python IDE (via MCPAgent)

* ✔ Streamlit Chat UI (visual interface)

* ✔ Any MCP-compatible LLM client

#| Component        | Description                                          |
 | ---------------- | ---------------------------------------------------- |
 | MCP Server       | Built using `fastmcp`, exposes the `get_alerts` tool |
 | Weather Tool     | Fetches active alerts from the official NWS API      |
 | Streamlit Client | Interactive chat UI powered by `MCPAgent`            |
 | Memory Support   | Agent remembers previous conversation context        |
 | API Safety       | Fully async with timeout + error handling            |
