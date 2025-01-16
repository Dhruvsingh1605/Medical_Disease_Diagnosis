from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

# Configure the GenAI API key
genai.configure(api_key="AIzaSyCgFnU3-1RMKeInY5PuhqoER2FUjUZaAtU")

app = Flask(__name__)

def predict_disease(combined_input):
    prompt = f"""
    You are a medical assistant AI. A user has shared their symptoms and additional information in natural language.
    Analyze the symptoms and additional information, predict the most likely disease or conditions, and recommend if they should see a doctor.

    User Input: "{combined_input}"

    Output Format:
    - Possible Disease:
    - Advice:
    - Diet:
    - Precautions:
    - Medication:
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

@app.route('/page1', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        input_text = request.form.get('textInput', '')
        return redirect(url_for('page2', input1=input_text))
    return render_template('Front-End_1.html')

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    input1 = request.args.get('input1', '')
    if request.method == 'POST':
        answers = {key: request.form[key] for key in request.form}
        combined_input = input1 + ' ' + ' '.join(answers.values())
        return redirect(url_for('page3', combined_input=combined_input))
    return render_template('Front-End_2.html', input1=input1)

@app.route('/page3', methods=['GET'])
def page3():
    combined_input = request.args.get('combined_input', '')
    prediction = predict_disease(combined_input)
    return render_template('Front-End_3.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
