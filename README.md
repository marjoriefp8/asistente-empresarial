# Enterprise AI Assistant

An advanced enterprise chatbot built with Anthropic's Claude AI, integrating Retrieval-Augmented Generation (RAG), autonomous agents, and persistent conversation memory.

## Key Features
- **Retrieval-Augmented Generation (RAG):** Delivers context-aware answers grounded exclusively in proprietary company documentation.
- **Agentic Workflow:** Dynamically executes specialized tools for mathematical computations and contact/directory lookups.
- **Persistent Conversation Memory:** Maintains full session context across multi-turn interactions.
- **Web Interface:** Powered by a clean, responsive Flask frontend.

## Tech Stack
- **Language:** Python
- **LLM Engine:** Anthropic Claude API (Function Calling & Tool Orchestration)
- **Embeddings & Vectorization:** Sentence Transformers (Local semantic search)
- **Web Framework:** Flask

## Deployment Strategy
This project is architected for local execution. The `sentence-transformers` module relies on PyTorch, which exceeds the 512MB RAM threshold of standard free hosting tiers (e.g., Render, Railway). 

For lightweight, live-deployed demonstrations utilizing lower memory footprints, please refer to my other repositories: [`analizador-pdf`](https://github.com/marjoriefp8/analizador-pdf) and [`agenteWeb`](https://github.com/marjoriefp8/agenteWeb).

## Installation & Setup
1. Clone the repository.
2. Install the required dependencies:  
   `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your API key:  
   `ANTHROPIC_API_KEY=your_actual_api_key_here`
4. Run the application:  
   `python app.py`
5. Open your browser and navigate to: `http://127.0.0.1:5000`
