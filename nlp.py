import openai
from transformers import pipeline

class NLP:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.sentiment_pipeline = pipeline("sentiment-analysis")
        self.ner_pipeline = pipeline("ner", grouped_entities=True)

    def generate_response(self, context, user_input):
        prompt = f"Context: {context}\n\nQuestion: {user_input}\nAnswer:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def analyze_sentiment(self, text):
        sentiments = self.sentiment_pipeline(text)
        return sentiments

    def recognize_entities(self, text):
        entities = self.ner_pipeline(text)
        return entities
