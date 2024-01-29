import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from log_config import logging
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from htmlTemplates import css, bot_template, user_template

# load_dotenv()
# os.environ['OPENAI_API_KEY'] = os.getenv('OPEN_API_KEY')

# Provide your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'YOUR OPENAI API KEY'

def get_pdf_text(pdf_docs):
    text = ""
    for pdf_doc in pdf_docs:
        reader = PdfReader(pdf_doc)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)
    return conversation_chain

def handle_user_question(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace('{{MSG}}', message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace('{{MSG}}', message.content), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Chat with PDFs", page_icon=":books:", layout="wide")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_user_question(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs file :books:", type=["pdf"], accept_multiple_files=True)
        st.write('Select Upload to start processing')
        if st.button("Upload"):
            logging.info("PDFs uploaded")
            logging.info("Processing started")
            with st.spinner("Processing"):
                #loading pdf
                logging.info("Getting raw data from PDFs")
                raw_text = get_pdf_text(pdf_docs)

                #chunk the loaded text
                logging.info("Chunking the raw text")
                text_chunks = get_text_chunks(raw_text)

                #creating vectorstore
                logging.info("Creating vectorstore")
                vectorstore = get_vectorstore(text_chunks)

                #create conversation chain
                logging.info("Creating a Conversational Chain")
                st.session_state.conversation = get_conversation_chain(vectorstore)


if __name__ == "__main__":
    main()