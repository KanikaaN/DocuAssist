
```
# Ramayana AI Assistant

This project implements an AI assistant using Streamlit for interaction. The assistant is designed to provide information and answer questions related to the Ramayana, an ancient Indian epic.

## Overview

The Ramayana AI Assistant is built using various technologies and APIs to enhance its functionality. It provides the following features:

- Text input: Users can input their queries or questions related to the Ramayana using the text input box.
- Response generation: The assistant generates responses based on the provided query using the GPT-3.5 model by OpenAI.
- Translation: Responses can be translated into Hindi using the Opus-MT-EN-HI model.
- Text-to-Speech (TTS): The original response can be converted into audio using the MMS-TTS-ENG model.
- PDF Reading: The assistant reads the content of a provided PDF file (in this case, "RAMAYANA.pdf") to gather information about the Ramayana.

## Installation

1. Clone the repository:

```
git clone <repository-url>
cd <repository-directory>
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Run the Streamlit app:

```
streamlit run app.py
```

4. Access the app in your web browser at `http://localhost:8501`.

## Usage

1. Upon running the app, you'll see the input field where you can enter your query related to the Ramayana.
2. After entering your query, the app will display the assistant's response along with a translation in Hindi (if available).
3. You can also listen to the response by clicking on the audio player.
4. The progress bar indicates the status of each step in processing your query, from retrieving passages to generating the response and translating it.

## API Keys

This project utilizes several APIs for NLP, translation, and text-to-speech. Ensure that you have the necessary API keys and configure them properly in the code.

- OpenAI API Key: Required for using the GPT-3.5 model for response generation.
- Hugging Face API Keys: Required for translation (Opus-MT-EN-HI) and text-to-speech (MMS-TTS-ENG) models.

## Credits

- Streamlit: For the interactive web app framework.
- OpenAI: For providing the GPT-3.5 model.
- Hugging Face: For providing the translation and text-to-speech models.
- PyPDF2: For PDF reading functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
