# Architecture Overview

This fake enterprise application represents an internal AI assistant used by ACME Bank engineering teams.

## Logical Flow

```text
Developer
  ↓
Cursor AI Coding Assistant
  ↓
GitHub MCP Server
  ↓
GitHub Repository: acme-finance-ai-platform
```

When Prompt Security Agentic AI is deployed, MCP activity should flow through the MCP Gateway:

```text
Cursor
  ↓
Prompt Security MCP Gateway
  ↓
GitHub MCP Server
  ↓
GitHub API
```

## Components

- FastAPI demo application
- Docker container example
- Kubernetes deployment examples
- Terraform infrastructure examples
- GitHub repository workflow
- Fake secrets and fake sensitive values for safe testing

## Demo Goal

Use Cursor with GitHub MCP to inspect this repository, create issues, summarize files, and generate Prompt Security Agentic AI visibility in Inventory and Activity Monitor.
