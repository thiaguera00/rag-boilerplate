# 🧠 RAG Chatbot Boilerplate — FastAPI + LangChain + WebSocket + OPENAI

Este é um boilerplate completo para construir aplicações conversacionais com **LLMs (Large Language Models)** usando a arquitetura **RAG (Retrieval-Augmented Generation)** integrada a um **MCP Server** via **Function Calling**, com comunicação em tempo real via **WebSocket**.

> Ideal para aplicações como assistentes virtuais, chatbots empresariais, atendimento médico automatizado e muito mais.

---

## 📌 Tecnologias Utilizadas

- 🐍 **Python 3.10+**
- ⚡️ **FastAPI** — API REST + WebSocket
- 🔗 **LangChain** — pipeline RAG, tools e agentes
- 🧠 **OpenAI API** — LLM + embeddings
- 🗃 **FAISS** — banco vetorial local
- 🔧 **Function Calling** — integração dinâmica com serviços

---

## 🧱 Estrutura do Projeto
```bash
├── app/ # WebSocket + FastAPI app
│ ├── main.py
│ ├── routes/
│ │ ├── websocket.py
│ │ └── health.py
├── services/ # Lógica do bot, agents, tools
│ ├── bot_service.py
│ ├── bot_tools.py
├── infrastructure/ # Integrações externas (LLM, vetorstore)
│ ├── rag_pipeline.py
│ ├── llm_client.py
├── utils/ # Configurações, utilitários
│ ├── config.py
│ ├── utils.py
├── base.txt # Base de conhecimento usada no RAG
├── .env.example # Exemplo das variáveis de ambiente
├── requirements.txt
└── README.md
```

## ⚙ Configurações do projeto

É necessário uma API KEY da OPENAI para utilizar a LLM, atualmente o RAG é feito utilizando uma base de conhecimento do tipo txt na raiz do projeto onde é necessário criar essa base de conhecimento e colocar na raiz do projeto.

## 🚀 Planos futuros

A ideia é ter suporte para adicionar a base de conhecimento para vários tipos como PDF docx e etc. </br>

