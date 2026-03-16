# 🤖 AI RAG Agent

---

## 🚀 Project Overview

AI RAG (Retrieval-Augmented Generation) Agent is a **document-based Q&A system** that allows users to upload PDFs or text files and ask questions.  

* Users can upload documents (PDF or TXT).  
* The system uses **retrieval + LLM generation** to provide context-aware answers.  
* Provides an interactive and responsive interface for easy use.

---

## 💡 Features

* **Document Upload**: Accepts PDFs and text files for processing.  
* **RAG Workflow**: Splits documents into chunks, embeds them, and stores in FAISS for fast retrieval.  
* **LLM-powered Answers**: Generates natural language responses using retrieved context.  
* **Vector Search**: Uses FAISS CPU for efficient similarity search.  
* **Interactive UI**: Built with Streamlit for responsive and intuitive interaction.  
* **Deployment-ready**: Can run locally or on Streamlit Cloud.

---

## 🛠️ Tech Stack

* **Backend & ML**: Python, LangChain  
* **Vector Database**: FAISS CPU  
* **Frontend**: Streamlit  
* **Logging & Utilities**: Rich, Markdown-it-py, Pygments  
* **Deployment**: Streamlit Cloud

---

## 🖥️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/meena1905/ai-rag-agent.git
cd ai-rag-agent

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py

# 5. Open in your browser
# http://localhost:8501
```
## 📌 Notes

RAG Approach: Combines document retrieval with LLM generation for accurate answers.

FAISS CPU: Efficient vector search for small to medium datasets.

Document Size: Large PDFs may take a few seconds for indexing.

Streamlit Integration: Frontend and backend in one app for easy deployment.

Deployment: Fully compatible with Streamlit Cloud.

---

## 🤝 Connect with Me

* [LinkedIn](https://linkedin.com/in/s-meenakshi-b2356b288)
  
---
