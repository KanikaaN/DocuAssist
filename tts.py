import requests

API_URL_TTS = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
headers_tts = {"Authorization": "Bearer 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"}

def query_tts(payload):
    response = requests.post(API_URL_TTS, headers=headers_tts, json=payload)
    return response.content
