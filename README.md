# Langchain2: Emotionally and Logically Adaptive Chatbot

This project is a Python chatbot that uses LangChain, LangGraph, and Anthropic's Claude model to provide responses tailored to the user's needs. The chatbot automatically classifies each user message as requiring either an emotional (therapist-style) or logical (fact-based) response, and routes the conversation accordingly.

## Features
- **Message Classification:** Uses an LLM to determine if a message needs an emotional or logical reply.
- **Therapist Agent:** Responds with empathy and emotional support for personal or sensitive topics.
- **Logical Agent:** Provides direct, factual, and logical answers for information-seeking queries.
- **Stateful Conversation:** Maintains conversation state and message history using LangGraph.

## Usage
1. Install dependencies in a Python 3.12+ environment (see `pyproject.toml`).
2. Set your Anthropic API key and any other required environment variables in a `.env` file.
3. Run the chatbot:
   ```bash
   python main.py
   ```
4. Type your message and the assistant will reply appropriately.

## Requirements
- Python 3.12+
- LangChain
- LangGraph
- Anthropic (Claude)
- python-dotenv

## License
MIT License
