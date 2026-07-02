---
title: AI Debate Arena
emoji: 🤖
sdk: gradio
sdk_version: "5.38.0"
app_file: app.py
---

# AI Debate Arena

A **Multi-Agent AI Debate System** where autonomous AI agents debate controversial topics, specialized judge agents independently evaluate the debate, and a consensus engine determines the final winner.

## Live Demo

🚀 **Try the deployed app here**

Hugging Face Demo:  
[Demo](https://varshithreddym-ai-debate.hf.space)

---

# Project Architecture

The system simulates a structured debate between autonomous AI agents.

```text
User enters debate topic
        ↓
PRO Agent generates argument
        ↓
ANTI Agent rebuts
        ↓
PRO Agent counter argues
        ↓
ANTI Agent final rebuttal
        ↓
Logic Judge evaluates reasoning
Evidence Judge checks factual strength
Practicality Judge checks feasibility
        ↓
Consensus voting engine determines winner
        ↓
Debate Analyzer summarizes strengths and weaknesses
```

---

# Features

- Autonomous PRO debating agent  
- Autonomous ANTI debating agent  
- Multi-round debate simulation  
- Independent Logic Judge  
- Independent Evidence Judge  
- Independent Practicality Judge  
- Final consensus voting engine  
- Debate analyzer for final reasoning breakdown  
- Public cloud deployment with web UI  

---

# Tech Stack

## Backend

- Python  
- OpenRouter API  
- OpenAI Python SDK  

## Frontend

- Gradio  

## AI System Design

- Multi-Agent Orchestration  
- Adversarial Reasoning  
- Autonomous Evaluation Pipeline  
- Consensus Voting Architecture  

## Deployment

- Hugging Face Spaces  
- Git + GitHub Version Control  

---

# Installation

Clone repository

```bash
git clone https://github.com/Varshith-Reddy-M/Multi-agent-AI-debate-system.git
```

Move into project

```bash
cd Multi-agent-AI-debate-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Locally

Run application

```bash
python app.py
```

or

```bash
python main.py
```

depending on your entrypoint.

---

# Example Debate Topics

- Should AI replace software engineers?  
- Should college degrees matter for hiring?  
- Is remote work better than office work?  
- Should social media be regulated?  
- Should AGI development be slowed down?  

---

# Important Notice

⚠ This application currently uses **free-tier LLM APIs** through OpenRouter.

Due to provider limitations, users may occasionally experience:

- High latency  
- API rate limit errors  
- Temporary provider outages  
- Failed debate generation in rare cases  

If this happens, retry after some time.

---

# Future Improvements

- Real-time streaming token generation in UI  
- Parallel judge execution for lower latency  
- PDF export of debate transcript  
- Debate history storage database  
- Multi-model comparison mode  
- User accounts and saved debates  

---

# Why this project matters

This project demonstrates practical engineering skills in:

- Multi-Agent AI Systems  
- LLM Orchestration  
- Prompt Engineering  
- API Integration  
- Cloud Deployment  
- Production Error Handling  
- Distributed Decision Architecture  

---

Built as an experimental autonomous reasoning system.