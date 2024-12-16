from flask import Flask, request, jsonify, render_template
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data['text']
    detected_language = detect(text)
    translator = Translator()

    if detected_language == 'en':
        translated_text = translator.translate(text, dest='te').text
    else:
        translated_text = text  # If not English, return the original text

    return jsonify({
        'detectedLanguage': detected_language,
        'translatedText': translated_text
    })

if __name__ == '__main__':
    app.run(debug=True)
