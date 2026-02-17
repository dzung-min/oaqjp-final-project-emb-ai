'''
Emotion detecting module
'''

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Send text to IBM Watson NLP model for analyzing
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, headers=headers, json=myobj)
    emotions = json.loads(res.text)["emotionPredictions"][0]["emotion"]
    max_score = 0
    dominant_emotion = ""
    for emotion, score in emotions.items():
        if max_score < score:
            max_score = score
            dominant_emotion = emotion
    emotions["dominant_emotion"] = dominant_emotion
    return emotions
