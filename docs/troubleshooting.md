# Troubleshooting

## Cursor cannot access GitHub MCP

- Confirm the GitHub MCP server is enabled in Cursor.
- Confirm the GitHub PAT is valid.
- Confirm the PAT has repo and read:user permissions.
- Restart Cursor after editing mcp.json.

## Prompt Security Inventory does not show GitHub MCP

- Confirm Prompt Security Agent is installed.
- Confirm Agentic AI/MCP Gateway is enabled.
- Confirm Cursor is a supported MCP client.
- Generate an MCP tool call, not only a normal chat prompt.
- Wait a few minutes for Inventory refresh.

## Activity Monitor does not show tool calls

- Use Agent mode in Cursor.
- Explicitly ask Cursor to use the GitHub MCP server.
- Allow tool execution when Cursor prompts.
- Search Activity Monitor for Cursor, GitHub, or MCP.
