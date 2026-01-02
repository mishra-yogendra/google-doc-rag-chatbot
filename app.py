import streamlit as st
from services.google_docs import fetch_google_doc
from services.vector_store import build_vector_store, load_vector_store
from services.groq_client import get_groq_client, ask_groq
from services.rag_chain import build_prompt

st.set_page_config("Google Doc AI Chatbot", layout="wide")
st.title("📄🤖 Google Doc AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = ""

# Sidebar
with st.sidebar:
    api_key = st.text_input("Groq API Key", type="password")
    doc_url = st.text_input("Public Google Doc URL")

    if st.button("Load Document"):
        try:
            docs = fetch_google_doc(doc_url)
            st.session_state.db = build_vector_store(docs)
            st.success("Document indexed successfully")
        except Exception as e:
            st.error(str(e))

question = st.text_input("Ask a question")

if st.button("Ask"):
    if not api_key:
        st.error("Enter Groq API key")
    elif "db" not in st.session_state:
        st.error("Load document first")
    else:
        retriever = st.session_state.db.as_retriever(k=3)
        docs = retriever.invoke(question)

        if not docs:
            st.write("This information isn't in the document.")
        else:
            prompt = build_prompt(
                question,
                docs,
                st.session_state.history[-2000:]
            )

            client = get_groq_client(api_key)
            answer = ask_groq(client, prompt)

            st.session_state.history += f"\nUser: {question}\nAI: {answer}\n"
            st.markdown(answer)
