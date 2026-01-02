# Google Doc AI Chatbot (RAG-based)

An AI-powered chatbot that reads content directly from a **public Google Doc** and answers user questions based strictly on the document.  
The system uses a **Retrieval-Augmented Generation (RAG)** architecture with vector search and an LLM to provide accurate, cited, and context-aware responses.

---

## 🚀 Features

- 📄 **Google Docs ingestion** (no manual copy-paste)
- 🧠 **Semantic search** using embeddings + FAISS
- 🤖 **LLM-powered answers** using LLaMA-3 via Groq
- 📌 **Inline citations** (e.g., Section 2)
- 💬 **Multi-turn conversation** with memory
- 🛡️ **Graceful handling of edge cases**
- ☁️ **Hosted online** using Streamlit Cloud



## 🏗️ Architecture (RAG Pipeline)
```
Google Doc (Public)
       ↓
Google Docs Export API
       ↓
Text Parsing & Chunking
       ↓
Embeddings (Sentence Transformers)
       ↓
FAISS Vector Store
       ↓
Top-3 Chunk Retrieval
       ↓
LLM (Groq – LLaMA-3)
       ↓
Streamlit Chat UI
```
---
## 📂 Project Structure

```

google-doc-rag-chatbot/
│
├── app.py
├── requirements.txt
├── runtime.txt
│
├── services/
│   ├── google_docs.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── groq_client.py
│   └── rag_chain.py
│
└── data/
└── faiss_index/

````

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd google-doc-rag-chatbot
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run locally

```bash
streamlit run app.py
```

---

## 🔑 Usage Instructions

1. Make sure the Google Doc is set to:
   **Share → Anyone with the link → Viewer**
2. Open the app
3. Enter:

   * Groq API Key
   * Public Google Doc link
4. Click **Load Document**
5. Ask questions in natural language

---

## 🧪 Edge Case Handling

| Scenario            | Behavior                                             |
| ------------------- | ---------------------------------------------------- |
| Private document    | Prompts user to share publicly                       |
| Empty document      | Shows error                                          |
| Irrelevant question | Responds: “This information is not in the document.” |
| Ambiguous query     | Requests clarification                               |
| Rate limits         | Gracefully handled                                   |

---

## 🧠 Technologies Used

* **Streamlit** – UI & hosting
* **FAISS** – Vector search
* **Sentence Transformers** – Embeddings
* **Groq (LLaMA-3)** – Language model
* **Google Docs Export API** – Document ingestion

---

## 🌐 Deployment

The chatbot is deployed on **Streamlit Cloud** and accessible via a public link.

> 🔗 *Deployment link:*
> https://app-doc-rag-chatbot.streamlit.app/

---
