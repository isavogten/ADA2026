from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams, McpToolset

load_dotenv()
"""Creates an ADK Agent equipped with tools from the MCP Server."""
tools =  McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://localhost:5000/mcp",timeout=600.0
            ),
            # Optional: Filter which tools from the MCP server are exposed
            # tool_filter=['list_directory', 'read_file']
        )

root_agent = LlmAgent(
    name="delivery_service_agent",
    model="gemini-2.5-flash-lite",
    description="Agent that manage order deliveries. ",
    instruction="You are an order delivery management expert specializing in creating, retrieving, updating, and deleting delivery records in the given context.",
    tools=[tools],
)
