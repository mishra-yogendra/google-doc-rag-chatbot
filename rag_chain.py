def build_prompt(question, docs, history):
    context = "\n\n".join(
        f"[{d.metadata['section']}]\n{d.page_content}"
        for d in docs
    )

    return f"""
You are an AI assistant answering ONLY from the document.

Conversation history:
{history}

Context:
{context}

Question:
{question}

Rules:
- If answer not found, say: "This information is not in the document."
- Always cite sections like (Section 2).
- Be concise.
"""
