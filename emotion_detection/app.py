from flask import Flask, request, jsonify
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    response = classifier(data['text'])
    return jsonify(response)
    
# if __name__ == '__main__':
#     app.run(debug=True)