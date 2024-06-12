
# DocuAssist: Your Document Assistant

DocuAssist is an application designed to assist users in exploring and learning from various documents. In this instance, it focuses on the ancient Indian epic, the Ramayana. Leveraging natural language processing (NLP), translation services, and text-to-speech (TTS) technology, DocuAssist provides an interactive platform for users to delve into the depths of the Ramayana.

## Features

- **Text Input:** Users can input queries or questions related to the Ramayana using the provided text input interface.
- **Response Generation:** DocuAssist generates responses based on the input query using the powerful GPT-3.5 model by OpenAI.
- **Translation:** Responses can be translated into Hindi using the Opus-MT-EN-HI translation model.
- **Text-to-Speech (TTS):** The generated response can be converted into audio using the MMS-TTS-ENG text-to-speech model.
- **PDF Reading:** DocuAssist reads the content of the provided PDF file ("Ramayana.pdf") to extract information about the Ramayana.

## Installation

1. Clone the repository:

```sh
git clone <repository-url>
cd <repository-directory>
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

3. Create a `secrets.toml` file in the `.streamlit` directory:

```sh
cd .streamlit
touch secrets.toml
```

4. Open the `secrets.toml` file and add your API keys in the following format:

```toml
[openai]
api_key = "YOUR_OPENAI_API_KEY"

[huggingface]
translation_api_key = "YOUR_HUGGINGFACE_TRANSLATION_API_KEY"
tts_api_key = "YOUR_HUGGINGFACE_TTS_API_KEY"
```

5. Run the Streamlit app:

```sh
streamlit run app.py
```

6. Access the app in your web browser at `http://localhost:8501`.

## Usage

1. Upon running the app, you'll see a text input field where you can enter your query related to the Ramayana.
2. After entering your query, DocuAssist will display the response along with a translation in Hindi (if available).
3. You can listen to the response audio by clicking on the provided audio player.
4. The progress bar indicates the status of each step in processing your query, from retrieving passages to generating the response and translating it.

## API Keys

This project requires API keys for accessing various services:

- **OpenAI API Key:** Required for using the GPT-3.5 model for response generation.
- **Hugging Face API Keys:** Required for translation (Opus-MT-EN-HI) and text-to-speech (MMS-TTS-ENG) models.

Ensure that you have the necessary API keys and configure them properly in the `secrets.toml` file.

## Credits

- **Streamlit:** For providing an easy-to-use web app framework.
- **OpenAI:** For providing the powerful GPT-3.5 model.
- **Hugging Face:** For providing the translation and text-to-speech models.
- **PyPDF2:** For PDF reading functionality.

