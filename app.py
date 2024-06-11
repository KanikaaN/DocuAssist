import streamlit as st
from utils import read_pdf
from rag import RAG
from nlp import NLP
import openai  # Import the openai module

# Load the PDF and initialize components
pdf_path = "RAMAYANA.pdf"
ramayana_text = read_pdf(pdf_path)
rag = RAG(ramayana_text)
OPENAI_API_KEY = "sk-proj-SpqXJZQpGuZ5uDGIJANwT3BlbkFJ1GgCE5QbQ9hpHhDTjGxW"
openai.api_key = OPENAI_API_KEY  # Set the OpenAI API key
nlp = NLP(openai.api_key)

st.title("RAG-powered ChatGPT with Sentiment Analysis and Entity Recognition")

user_input = st.text_input("You:", "Tell me about Rama's birth")
if user_input:
    passages = rag.retrieve_passages(user_input)
    context = " ".join(passages)
    response = nlp.generate_response(context, user_input)
    st.write("ChatGPT:", response)

    sentiments = nlp.analyze_sentiment(response)
    st.write("Sentiment:", sentiments)

    entities = nlp.recognize_entities(response)
    st.write("Entities:", entities)
