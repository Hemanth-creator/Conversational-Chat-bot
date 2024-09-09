## Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
import replicateresponse
## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os


if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

## Function to load OpenAI model and get respones

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer =  replicateresponse.chat(question)
    st.session_state['flowmessages'].append(AIMessage(content=answer))
    return answer

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)