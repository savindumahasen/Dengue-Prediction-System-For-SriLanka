from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Change the path to the local path where your model is stored
model_path = './DengueDetectionModel.h5'
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dengueprediction', methods=['POST'])
def predict():
    feature_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    try:
        features = [float(request.form[f]) for f in feature_names]
    except ValueError:
        return jsonify({'error': 'Invalid input'})

    input_data = [features]

    # Make prediction
    pred = model.predict(input_data)
    prob = model.predict_proba(input_data)[0]

    # Display the result
    if pred[0] == 0:
        result = "Dengue Not Infected"
    else:
        result = "Dengue Infected"

    return jsonify({'result': result, 'probability': prob[1]})

if __name__ == '__main__':
    app.run(debug=True)
