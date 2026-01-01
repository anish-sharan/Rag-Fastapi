import os
from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embeddings

VECTOR_PATH = "app/storage/faiss_index"
INDEX_FILE = os.path.join(VECTOR_PATH, "index.faiss")


def save_vector_store(chunks):
    embeddings = get_embeddings()
    os.makedirs(VECTOR_PATH, exist_ok=True)

    # First upload → create index
    if not os.path.exists(INDEX_FILE):
        db = FAISS.from_documents(chunks, embeddings)
    else:
        db = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        db.add_documents(chunks)

    db.save_local(VECTOR_PATH)


# ✅ NEW FUNCTION: load_vectorstore
def load_vectorstore(path=VECTOR_PATH):
    embeddings = get_embeddings()
    if os.path.exists(os.path.join(path, "index.faiss")):
        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        # Return empty FAISS DB if nothing exists yet
        return FAISS.from_documents([], embeddings)
