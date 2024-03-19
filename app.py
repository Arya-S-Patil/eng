#bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = apikey

#app framework
st.title("Language Learning System")
prompt=st.text_input("Plug in your code here")