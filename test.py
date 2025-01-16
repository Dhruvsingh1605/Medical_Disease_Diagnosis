import json

def load_input_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            symptoms_info = data.get('inputText', '')
            return symptoms_info
    except Exception as e:
        return f"Error: Unable to load the input file. Details: {e}"
    
a = load_input_from_file('/media/dhruv/Local Disk/Speech_Trial/Front-End-Trial/medical_transcription.json')
print(a)