import os
from langchain_community.vectorstores import FAISS
from services.embeddings import get_embedding_model

DB_PATH = "data/faiss_index"

# -------- SIMPLE, SAFE TEXT SPLITTER --------
def split_documents(docs, chunk_size=800, overlap=150):
    chunks = []

    for doc in docs:
        text = doc.page_content
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append(
                type(doc)(
                    page_content=chunk_text,
                    metadata=doc.metadata
                )
            )

            start = end - overlap

    return chunks


def build_vector_store(docs):
    embeddings = get_embedding_model()

    chunks = split_documents(docs)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)
    return db


def load_vector_store():
    embeddings = get_embedding_model()

    if os.path.exists(DB_PATH):
        return FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return None
