# 🏥 Medical Assistant — RAG-Powered AI Health Q&A

> AI Medical Assistant that answers health questions using Retrieval-Augmented Generation (RAG).  
> Query embedding → FAISS retrieval → Google Gemini generation → safety validation.  
> Built with LangChain, Sentence Transformers, and Streamlit.  
> **NTI × ITIDA NLP Graduation Project | Score: 92.5%**

---

## 📌 Overview

Instead of sending a user's question directly to an LLM, this system first **retrieves relevant medical knowledge** from a curated dataset, then uses it as grounded context for generation.

This approach reduces hallucinations and keeps responses factual — which is critical in a healthcare setting.

---

## ⚙️ RAG Pipeline

```
User Query
    ↓
Query Embedding (Sentence Transformers - all-MiniLM-L6-v2)
    ↓
Semantic Search (FAISS Vector Index)
    ↓
Retrieved Medical Context (MedQuAD Dataset)
    ↓
Structured Prompt Construction
    ↓
Google Gemini Generation
    ↓
Safety Validation Layer
    ↓
Response to User
```

---

## 🛡️ Safety System

Because this is a healthcare-focused project, retrieval alone isn't enough. We designed multiple safety layers around the generation process:

| Layer | Description |
|---|---|
| 🚨 Emergency Detection | Detects critical situations and bypasses LLM with emergency-oriented response |
| 📋 Prompt Constraints | Model is instructed not to confirm diagnoses or provide dosage recommendations |
| 🔍 LLM Self-Review | Generated responses are reviewed for unsupported claims before delivery |
| ✅ Rule-Based Post-Processing | Deterministic safety rules applied independently of the model |

---

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Search | FAISS |
| LLM | Google Gemini |
| Orchestration | LangChain |
| Knowledge Base | MedQuAD Dataset |
| Interface | Streamlit |
| Language | Python |

---

## 🗂️ Project Structure

```
medical-assistant/
├── retrieval/          # Embedding + FAISS vector search
├── prompting/          # Prompt construction and templates
├── generation/         # Google Gemini integration
├── safety/             # Safety layers and post-processing
├── pipeline/           # End-to-end pipeline orchestration
├── tests/              # Unit tests for all components
└── app.py              # Streamlit interface
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Ahmed-Mohammed873/Medical-Assistant.git
cd Medical-Assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API key
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🧪 Tests

```bash
pytest tests/
```

Covers: retrieval, prompting, Gemini integration, safety layers, and full pipeline.


## 📄 License

MIT License
