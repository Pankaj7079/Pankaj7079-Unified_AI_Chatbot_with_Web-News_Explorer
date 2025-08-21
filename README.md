#  Unified AI Chatbot with Web & AI News Explorer

An **AI-powered chatbot** that unifies **LLMs, LangGraph, and Streamlit UI** into a single platform.
It not only chats with users but also **fetches real-time AI news and web information**, making it a powerful **AI + Web Explorer**.

---

##  Features

*  **Conversational AI Chatbot** powered by **LangGraph + LLMs**
*  **Web & AI News Fetcher** using custom tools integration
*  **Streamlit UI** for a clean and interactive user experience
*  Modular design with **nodes, states, and tools** for easy extension
*  Config-driven setup via `.ini` file

---

##  Tools & Technologies Used

* **[LangGraph](https://www.langchain.com/langgraph)** → For building agent workflows
* **LangChain** → LLMs orchestration and integration
* **Streamlit** → Interactive frontend UI
* **Python** → Core programming language
* **ConfigParser** → For managing app configuration
* **Custom Tools** → Web Scraping & AI News APIs

---

##  Project Structure

```bash
Unified-AI-Chatbot/
│── src/
│   ├── langgraphagenticai/     # Core chatbot package
│   │   ├── graph/              # LangGraph workflow definitions
│   │   ├── LLMS/               # LLM models & configs
│   │   ├── nodes/              # Graph nodes (logic units)
│   │   ├── state/              # State management
│   │   ├── tools/              # Tools (web search, AI news, etc.)
│   │   ├── ui/                 # Streamlit UI components
│   │   ├── __init__.py
│   │   ├── main.py             # Entry point for LangGraph app
│   ├── __init__.py
│── venv_chatbot/               # Virtual environment
│── app.py                      # Main entry for Streamlit UI
│── README.md                   # Documentation
│── .gitignore                  # Ignored files
```



## Usage

* Open your browser at `http://localhost:8501`
* Select your **LLM model** and **use case** from the dropdown
* Start chatting or explore **AI news & web search**

---

##  Future Enhancements

* Support for **multi-agent workflows**
* Integration with **voice input/output**
* More **AI-powered tools** (document Q\&A, summarization, etc.)

---
