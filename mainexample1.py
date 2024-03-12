## Integrate our code OpenAI API 

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain


import streamlit as st


os.environ["OPENAI_API_KEY"]=openai_key
# streamlit framework


st.title('LLM Chat bot with Open API')
input_text=st.text_input('Search the topic you want')



# Prompt template 

first_input_prompt=PromptTemplate(
  input_variables=['name'], 
  template="Tell me about {name}"
)
llm=OpenAI(temperature=0.8)

chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='title')










if input_text:
  st.write(chan.run(input_text))