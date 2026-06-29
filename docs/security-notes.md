# Security Notes

This repository is intentionally designed for a Prompt Security Agentic AI demo.

## Demo Security Topics

- Fake secrets in `.env.example`
- Kubernetes deployment review
- Terraform configuration review
- GitHub MCP repository inspection
- GitHub issue creation through MCP
- Agentic AI Activity Monitor validation

## Important Safety Notice

All secrets and credentials are fake. Do not place production credentials in this repository.

## Example Findings to Ask Cursor to Review

- Are there secrets in `.env.example`?
- Does the Kubernetes deployment use resource limits?
- Does the Dockerfile run as non-root?
- Are Terraform resources publicly exposed?
- What security improvements should be tracked in GitHub Issues?
