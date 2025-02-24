from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms import Ollama


def load_documents():
    document_loader = PyPDFLoader("./data/cudos-white-paper.pdf")
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
    print("question: ", question)
    # load the document
    docs = load_documents().load()

    print('docs: ', docs[0])

    # get documents in split chunks
    chunks = split_documents(docs)

    print('chunks: ', chunks)

    # pass chunks to vector db and retrieve the similarity with nearest of 3
    retriever = add_to_chroma_vector_db(chunks).as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # invoke the retriever with the question to get the similarity items
    retrieved_docs = retriever.invoke(question)

    # iterate over the retrieved_docs, get each page content and hold them as the context
    context = ' '.join([doc.page_content for doc in retrieved_docs])

    # initialize the LLM and model
    llm = Ollama(model="llama3.2")

    response = llm.invoke(f"""
        You are a cudos assistant. Provide a 500 maximum words and concise response to user\'s question.:
        Context: {context}
        Question: {question} 
    """)

    return response
