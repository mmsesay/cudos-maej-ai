from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms import Ollama


def load_documents():
    document_loader = PyPDFLoader("./data/Software Development Proposal NIC.pdf")
    return document_loader


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=8,
        length_function=len,
        is_separator_regex=False,
    )

    return text_splitter.split_documents(documents)


def get_embedding_function():
    return OllamaEmbeddings(model="all-minilm")


def add_to_chroma_vector_db(chunks: list[Document]):
    return Chroma.from_documents(documents=chunks, embedding=get_embedding_function())


def chain_retriever(question):
    docs = load_documents().load()
    chunks = split_documents(docs)

    retriever = add_to_chroma_vector_db(chunks).as_retriever(search_type="similarity", search_kwargs={"k": 3})
    retrieved_docs = retriever.invoke(question)

    context = ' '.join([doc.page_content for doc in retrieved_docs])

    llm = Ollama(model="llama3.2")
    response = llm.invoke(f"""Answer the question according to the context
        given very briefly: 
        Question: {question}.
        Context: {context}         
    """)

    return response


if __name__ == '__main__':
    chain = chain_retriever("what is the name of the frontend dev")

    print(chain)
