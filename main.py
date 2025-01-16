
from flask import Flask, jsonify
import json
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyCgFnU3-1RMKeInY5PuhqoER2FUjUZaAtU")

@app.route('/predict_disease', methods=['GET'])
def predict_disease():
    file_path = '/media/dhruv/Local Disk/Speech_Trial/Front-End-Trial/medical_transcription.json'
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            symptoms_info = data.get('inputText', '')
            if symptoms_info:
                prompt = f"""
                You are a medical assistant AI. A user has shared their symptoms and additional information in natural language.
                Analyze the symptoms and additional information, predict the most likely disease or conditions, and recommend if they should see a doctor.

                User Input: "{symptoms_info}"

                Output Format:
                - Possible Disease:
                - Advice:
                - Diet:
                - Precautions:
                - Medication:
                """
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt)
                return jsonify({'prediction': response.text})
            else:
                return jsonify({'prediction': 'No symptoms information provided in the input file.'})
    except Exception as e:
        return jsonify({'prediction': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
