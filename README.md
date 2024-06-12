
 Ramayana AI Assistant

The Ramayana AI Assistant is an application designed to assist users in learning about the ancient Indian epic, Ramayana. The application utilizes various natural language processing (NLP) techniques, translation services, and text-to-speech (TTS) technology to provide interactive responses to user queries.

## Features

- **Text Input:** Users can input their queries or questions related to the Ramayana using the provided text input interface.
- **Response Generation:** The assistant generates responses based on the provided query using the powerful GPT-3.5 model by OpenAI.
- **Translation:** Responses can be translated into Hindi using the Opus-MT-EN-HI translation model.
- **Text-to-Speech (TTS):** The original response can be converted into audio using the MMS-TTS-ENG text-to-speech model.
- **PDF Reading:** The application reads the content of the provided PDF file ("RAMAYANA.pdf") to gather information about the Ramayana.

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

3. Run the Streamlit app:

```sh
streamlit run app.py
```

4. Access the app in your web browser at `http://localhost:8501`.

## Usage

1. Upon running the app, you'll see a text input field where you can enter your query related to the Ramayana.
2. After entering your query, the app will display the assistant's response along with a translation in Hindi (if available).
3. You can listen to the response audio by clicking on the provided audio player.
4. The progress bar indicates the status of each step in processing your query, from retrieving passages to generating the response and translating it.

## API Keys

This project requires API keys for accessing various services:

- **OpenAI API Key:** Required for using the GPT-3.5 model for response generation.
- **Hugging Face API Keys:** Required for translation (Opus-MT-EN-HI) and text-to-speech (MMS-TTS-ENG) models.

Ensure that you have the necessary API keys and configure them properly in the code.

## Credits

- **Streamlit:** For providing an easy-to-use web app framework.
- **OpenAI:** For providing the powerful GPT-3.5 model.
- **Hugging Face:** For providing the translation and text-to-speech models.
- **PyPDF2:** For PDF reading functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to copy and paste this Markdown content into a file named `README.md` in your project directory. Adjust any placeholder values like `<repository-url>` and `<repository-directory>` with your actual repository URL and directory name.
