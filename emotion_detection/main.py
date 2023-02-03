from flask import Flask, request, jsonify
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
appv = Flask(__name__)

@appv.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    response = classifier(data['text'])
    return jsonify(response)
    