# AI IT Helpdesk Agent

An AI-powered IT Helpdesk Agent built using RAG, tools, and a local Ollama LLM.

## Features

- Retrieves troubleshooting information from a local knowledge base
- Uses embeddings for semantic search
- Uses Ollama and Qwen for response generation
- Performs basic system and internet diagnostics
- Supports interactive IT troubleshooting
- Runs locally without requiring a cloud LLM API

## Architecture

User
↓
Interactive Helpdesk Agent
↓
RAG + Diagnostic Tools
↓
Knowledge Base + System Diagnostics
↓
Qwen via Ollama
↓
Troubleshooting Response

## Technologies

- Python
- Ollama
- Qwen
- nomic-embed-text
- NumPy
- Retrieval-Augmented Generation (RAG)

## Project Structure

```text
ai-it-helpdesk-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── knowledge_base/
│   ├── password.txt
│   ├── printer.txt
│   ├── slow_computer.txt
│   └── wifi.txt
│
└── src/
    ├── __init__.py
    ├── agent.py
    ├── rag.py
    └── tools.py