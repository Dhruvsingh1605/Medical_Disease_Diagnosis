import pickle

def store_data_locally(input_data, filename='symptom_data.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(input_data, file)
        print("Data saved successfully")

input_data = "Sample medical voice input data"
store_data_locally(input_data)

def load_data_locally(filename='symptom_data.pkl'):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        print("No data found locally")
        return None
    
loaded_data = load_data_locally()
