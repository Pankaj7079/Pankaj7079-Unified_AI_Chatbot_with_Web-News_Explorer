# Unified AI Chatbot with Web & AI News Explorer

**Your all-in-one AI companion for smart conversations, real-time web search, and the latest AI news.**

---

## Overview

This project is a **unified AI chatbot** that combines the best of conversational AI, web exploration, and AI news updates.

Unlike a simple chatbot, this system uses multiple **state-of-the-art language models (LLMs)**, integrates real-time web search, and fetches up-to-date AI news — all inside one clean and interactive app.

Built with **LangGraph** for agent-based workflows and a sleek **Streamlit UI**, it’s designed to be both powerful and easy to use. Whether you want a casual conversation, the latest news on AI breakthroughs, or to search for specific information online, this chatbot has you covered.

---

##  Features

* ** Conversational AI** – Have natural, intelligent conversations powered by top LLMs.
* ** Web & AI News Explorer** – Search the web in real time or get the latest AI news at your fingertips.
* ** Multi-LLM Support** – Easily switch between different models based on your needs.
* ** Interactive UI** – A clean, modern interface built with Streamlit.
* ** Modular & Extensible** – Add new tools, nodes, or models with minimal effort.
* ** Configurable** – Simple `.ini` file to customize your chatbot’s setup.

---

##  How It Works

1. **Input** – You interact with the chatbot through the Streamlit interface.
2. **LangGraph Agent** – Your query is routed through a LangGraph agent, which decides the right tool to use.
3. **Tool Execution** – The agent can:

   * Perform a **Web Search** for real-time info
   * Fetch the latest **AI News**
   * Or just use the **Chatbot** directly
4. **LLM Processing** – The results are passed to your chosen LLM for deeper analysis.
5. **Response** – The chatbot generates a clear, thoughtful reply in the UI.

---

##  Tech Stack

* **Core:** [LangGraph](https://www.langchain.com/langgraph), [LangChain](https://www.langchain.com/), [Streamlit](https://streamlit.io/)
* **Language:** [Python](https://www.python.org/)

---

##  Models

Currently supported LLMs:

* **llama3-8b-8192** – Fast and efficient for most tasks.
* **llama-3.3-70b-versatile** – Larger, stronger reasoning model for complex queries.
* **gemma2-9b-it** – Instruction-tuned model with excellent conversational quality.

---

##  Tools

* **Tavily** – Accurate and powerful web search.
* **AI News API** – Fetches the latest AI-related articles and updates.
* **More coming soon** – Easy to extend with new tools.


---

## 🖥 Usage

* **Choose your model** – Select from the supported LLMs.
* **Pick your use case** – Chat, get AI news, or search the web.
* **Start chatting** – Type a message and hit Enter.

---

##  Future Plans

* Multi-agent workflows for advanced reasoning.
* Voice input/output for natural conversations.
* More AI-powered tools (document Q\&A, summarization, code generation, etc).

---

##  Contributing

Contributions are welcome! Feel free to open an issue or PR if you’d like to improve the chatbot.


---

##  Acknowledgments

* [LangChain](https://www.langchain.com/)
* [LangGraph](https://www.langchain.com/langgraph)
* [Streamlit](https://streamlit.io/)
* And the wider open-source community.

---
