# ChatPDF
Welcome to the ChatPDF repository! This project is designed to provide a seamless experience for querying information from your PDF files. Whether you need specific answers based on the content of your PDF or want to engage in general conversation with a chatbot, ChatPDF has got you covered.

## Features
* PDF Upload: Easily upload one or multiple PDF files to extract information.
* Contextual Queries: Query the system to get answers based on the context provided by your PDF files.
* General Conversation: Use ChatPDF for casual and general conversations with the integrated chatbot (But first upload your pdf).
* Powered by LangChain: Interaction with Large Language Models (LLM) is facilitated through LangChain.
* Interactive Web App: Utilizes Streamlit, a Python library for creating interactive web applications.

## Getting Started
To run this project locally, follow these simple steps:
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/AashishChapain/chatpdf.git
    ```
2. Navigate to the project directory:
    ```bash
    cd CHAT_PDF
    ```
3. Install the required dependencies. It's recommended to use a virtual environment
    ```bash
    pip install -r requirements.txt
    ```
4. Load your OpenAI API Key in app.py:
    ```bash
    os.environ['OPENAI_API_KEY'] = 'YOUR OPENAI API KEY'
    ```
5. Run the streamlit application using the following command:
    ```bash
    streamlit run app.py
    ```

**Note:** Please upload your CSV to get started.