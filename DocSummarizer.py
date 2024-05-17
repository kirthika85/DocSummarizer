import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
summarised_text=""

st.title("Document Summarizer")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
if not openai_api_key.startswith('sk-'):
   st.warning('Please enter your OpenAI API key!', icon='⚠')
if openai_api_key.startswith('sk-'):
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
       st.write("### Uploaded Document Contents:")
       file_contents = uploaded_file.read().decode("utf-8")
       st.write(file_contents)
       summarize_button=st.button("Summarize")   
       if summarize_button:
          llm=ChatOpenAI(api_key=openai_api_key,temperature=0.1,model_name="gpt-3.5-turbo")
          prompt=ChatPromptTemplate.from_template(file_contents)
          response=prompt|llm
          print(response)
          summarised_text=ChatPromptTemplate.from_messages
          st.write("### Summarized Document:")
          #template_start_index=response.find("template='")+len("template='")
          #template_end_index = response.find("',", template_start_index)
          #template_text = template[template_start_index:template_end_index]
          #template_text = template_text.replace("\\r\\n", "\n")
          st.write(summarised_text)
