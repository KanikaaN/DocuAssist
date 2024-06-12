import streamlit as st
from utils import read_pdf
from rag import RAG
from nlp import NLP
from translation import translate_text
from tts import query_tts

def main():
    # Load the PDF and initialize components
    pdf_path = "RAMAYANA.pdf"
    ramayana_text = read_pdf(pdf_path)
    rag = RAG(ramayana_text)
    OPENAI_API_KEY = "sk-proj-jeYFCV7kTq4giBPNk7yQT3BlbkFJOZl5SdWoYsl12uMQd4EB"
    nlp = NLP(OPENAI_API_KEY)

    st.title("Ramayana AI Assistant")

    user_input = st.text_input("You:", "Tell me about Rama's birth")
    if user_input:
        # Initialize progress bar and spinner
        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("Retrieving passages...")
        with st.spinner("Retrieving passages..."):
            passages = rag.retrieve_passages(user_input)
        context = " ".join(passages)
        progress_bar.progress(33)

        status_text.text("Generating response...")
        with st.spinner("Generating response..."):
            response = nlp.generate_response(context, user_input)
        progress_bar.progress(66)

        status_text.text("Translating response to Hindi...")
        with st.spinner("Translating response to Hindi..."):
            translated_response = translate_text({"inputs": response})
        progress_bar.progress(99)

        # Create two columns
        col1, col2 = st.columns(2)

        # Display the original response and the translated response in separate columns
        with col1:
            st.header("Assistant Response")
            st.write(response)

        with col2:
            st.header("Translated Response (Hindi)")
            if 'error' in translated_response:
                st.write(translated_response['error'])
                st.write(translated_response['content'])
            elif isinstance(translated_response, list) and len(translated_response) > 0 and 'translation_text' in translated_response[0]:
                st.write(translated_response[0]['translation_text'])
            else:
                st.write("Unexpected response format:")
                st.write(translated_response)

        # Update the progress bar to 100% after displaying the results
        progress_bar.progress(100)
        status_text.text("Completed")

        # Generate TTS for the original response
        status_text.text("Generating TTS...")
        with st.spinner("Generating TTS..."):
            audio_bytes = query_tts({"inputs": response})
        st.audio(audio_bytes, format="audio/wav")

        # Remove the "Generating TTS..." message
        status_text.empty()

if __name__ == "__main__":
    main()