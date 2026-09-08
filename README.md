# 🖥️ AI IT Helpdesk Agent

An edge-optimized, agentic IT support assistant developed to triage, route, and resolve Tier-1 technical support queries locally. Built using **LangGraph**, **FAISS**, **Ollama (`llama3.2:1b`)**, and **Streamlit** without relying on paid external cloud APIs.

---

## 🚀 Key Features

- **Local & Private:** Runs entirely on local CPU memory using Ollama, providing data privacy and zero API token costs.

- **Smart Gatekeeping:** Uses rule-based and LLM-assisted validation to identify IT-related questions and reject non-IT queries.

- **Hybrid Retrieval:**
  - **Local SOPs/Runbooks:** FAISS vector similarity search across pre-indexed internal troubleshooting guides.
  - **Dynamic Web Search:** Uses DuckDuckGo as a fallback when relevant documentation is not available locally.

- **CPU Optimized:** Uses a lightweight Ollama model with optimized context and output limits for faster responses on standard laptops.

- **Interactive UI:** Provides a Streamlit interface for submitting IT issues and receiving troubleshooting solutions.

---

## 🛠️ Architecture Workflow

```text
[User Input]
      │
      ▼
[Gatekeeper Node]
      │
      ├── (Non-IT) ──► [Reject Node] ──► [End]
      │
      │
      └── (IT Issue)
              │
              ▼
      [FAISS Local Retriever]
              │
              ├── (Relevant Document Found)
              │              │
              │              ▼
              │      [Generate Solution Node]
              │              │
              │              ▼
              │           [Output]
              │
              └── (Document Missing)
                             │
                             ▼
                  [DuckDuckGo Web Search]
                             │
                             ▼
                  [Generate Solution Node]
                             │
                             ▼
                          [Output]
🧰 Tech Stack
Technology	Purpose
Python	Application development
LangGraph	Agent workflow and routing
LangChain	LLM and retrieval integration
Ollama	Local LLM execution
Llama 3.2 1B	Local language model
FAISS	Vector similarity search
HuggingFace Sentence Transformers	Text embeddings
DuckDuckGo Search	Web search fallback
Streamlit	Interactive user interface
📂 Project Structure
AI-IT-Helpdesk-Agent/
│
├── app/
│   ├── graph.py          # LangGraph state machine and routing logic
│   └── state.py          # Agent state schema
│
├── data/
│   ├── hardware/         # Hardware troubleshooting runbooks
│   ├── network/          # Network troubleshooting runbooks
│   ├── software/         # Software troubleshooting guides
│   └── wifi/             # Wi-Fi troubleshooting guides
│
├── scripts/
│   ├── ingest.py         # Builds the FAISS vector database
│   └── add_doc.py        # Adds individual documents
│
├── app_ui.py             # Streamlit frontend
├── main.py               # Terminal application runner
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
⚡ Setup & Installation
1. Clone the Repository
git clone https://github.com/mercyselvan/ai-it-helpdesk-agent.git
cd AI-IT-Helpdesk-Agent
2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Install and Pull Ollama Model

Make sure Ollama is installed and running on your system.

Pull the required model:

ollama pull llama3.2:1b
5. Build the Local Vector Database

Run the ingestion script to create the FAISS vector database from the local knowledge base:

python scripts/ingest.py
6. Run the Application

Start the Streamlit application:

python -m streamlit run app_ui.py --server.fileWatcherType none

Then open the application in your browser:

http://localhost:8501
🧠 How the System Works
The user enters an IT-related problem.
The Gatekeeper Node checks whether the query is an IT support request.
The system searches the local knowledge base using FAISS.
Relevant troubleshooting information is retrieved using semantic similarity.
If suitable local information is not found, the system performs a DuckDuckGo web search.
The retrieved context is passed to the local Llama 3.2 1B model through Ollama.
The system generates a troubleshooting response.
The final solution is displayed through the Streamlit interface.
📚 Knowledge Base

The project contains troubleshooting information for common IT support issues, including:

Hardware problems
Network problems
Wi-Fi issues
Software problems
General troubleshooting procedures

The documents are converted into embeddings and indexed in FAISS for semantic retrieval.

🔒 Privacy

This project is designed to run locally using Ollama. The core LLM inference does not require a paid cloud LLM API, making the system suitable for privacy-focused local IT support scenarios.

🎯 Use Cases

The AI IT Helpdesk Agent can assist users with:

Wi-Fi connectivity problems
Network troubleshooting
Slow computer issues
Hardware-related problems
Software troubleshooting
Basic IT support questions
Step-by-step troubleshooting guidance
🔮 Future Enhancements

Possible future improvements include:

Voice-based IT support
Ticket creation and management
User authentication
Advanced system diagnostics
More troubleshooting knowledge bases
Multi-language support
Conversation history
Integration with enterprise IT service management systems
