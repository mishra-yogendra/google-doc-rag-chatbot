import re
import requests
from langchain_core.documents import Document

def extract_doc_id(doc_url: str) -> str:
    """
    Extract Google Doc ID from multiple valid URL formats.
    """
    patterns = [
        r"/document/d/([a-zA-Z0-9-_]+)",
        r"id=([a-zA-Z0-9-_]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, doc_url)
        if match:
            return match.group(1)

    raise ValueError("Invalid Google Docs link. Please use a valid public Google Doc URL.")


def fetch_google_doc(doc_url: str):
    """
    Fetches Google Doc content using the export API.
    Document MUST be publicly shared.
    """
    doc_id = extract_doc_id(doc_url)

    export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    response = requests.get(export_url)

    if response.status_code != 200:
        raise PermissionError(
            "Document is private or inaccessible. "
            "Please set sharing to 'Anyone with the link can view'."
        )

    text = response.text.strip()
    if not text:
        raise ValueError("Document is empty.")

    sections = text.split("\n\n")

    docs = []
    for i, sec in enumerate(sections):
        docs.append(
            Document(
                page_content=sec,
                metadata={"section": f"Section {i+1}"}
            )
        )

    return docs
