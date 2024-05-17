import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def summarize_document(document):
      prompt = ChatPromptTemplate.from_template(document)
      response = prompt | openai.Completion.create(engine="text-davinci-002", max_tokens=150)
      summarized_text = response.choices[0].text.strip()
      return summarized_text

st.title("Document Summarizer")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
if generate_button and openai_api_key.startswith('sk-'):
    uploaded_file = st.file_uploader("Upload a document file", type=["txt", "pdf"])
    if uploaded_file is not None:
        st.write("### Uploaded Document Contents:")
        file_contents = uploaded_file.read().decode("utf-8")
        st.write(file_contents)
        if st.button("Summarize"):
           summarized_text = summarize_document(file_contents)
           st.write("### Summarized Document:")
            st.write(summarized_text)
