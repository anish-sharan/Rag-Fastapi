import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

VECTOR_PATH = "app/storage/faiss_index"

from app.rag.vector_store import load_vectorstore  # your FAISS loader

def get_qa_chain():
    # Load vector store
    vectorstore = load_vectorstore(VECTOR_PATH)

    # Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Prompt template
    prompt = PromptTemplate.from_template(
        """
        Answer the question based only on the context below.
        If you don't know, say you don't know.

        Context:
        {context}

        Question:
        {question}
        """
    )

    # OpenRouter LLM (via environment variables)
    llm = ChatOpenAI(
        model="mistralai/mixtral-8x7b-instruct",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )

    # Runnable pipeline: retriever → prompt → LLM
    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return chain
