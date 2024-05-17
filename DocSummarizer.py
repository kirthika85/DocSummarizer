import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

#def summarize_document(document):
  #prompt = ChatPromptTemplate.from_template(document)
  #    response = prompt | openai.Completion.create(engine="text-davinci-002", max_tokens=150)
   #   summarized_text = response.choices[0].text.strip()
    #  return summarized_text

st.title("Document Summarizer")
upload_button=st.button("UploadFile")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
#if not openai_api_key.startswith('sk-'):
   # st.warning('Please enter your OpenAI API key!', icon='⚠')
if upload_button:
   uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
   if uploaded_file is not None:
      st.write("### Uploaded Document Contents:")
      file_contents = uploaded_file.read().decode("utf-8")
      st.write(file_contents)
      #summarize_button=st.button("Summarize")   
      #if summarize_button:
       #  prompt=ChatPromptTemplate.from_template(file_contents)
        # response=prompt|openai.Completion.create(engine="text-davinci-002", max_tokens=150)
         #summarized_text = summarize_document(file_contents)
         #summarized_text = response.choices[0].text.strip()
         #st.write("### Summarized Document:")
         #st.write(summarized_text)
