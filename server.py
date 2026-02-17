"""
Entry point for the app
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Render homepage
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def get_response():
    """
    Analyze text and return the result
    """
    text_to_analyze = request.args.get("textToAnalyze")
    resp = emotion_detector(text_to_analyze)
    if not resp["dominant_emotion"]:
        return "<b>Invalid text! Please try again!</b>"
    return (
        f"For the given statement, the system response is "
        f"'anger': {resp['anger']}, 'disgust': {resp['disgust']}, "
        f"'fear': {resp['fear']}, 'joy': {resp['joy']} and "
        f"'sadness': {resp['sadness']}. The dominant emotion is "
        f"<b>{resp['dominant_emotion']}</b>."
    )
