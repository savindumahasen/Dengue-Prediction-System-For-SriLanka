from flask import Flask, render_template, request
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
    feature_names = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9', '10']

    try:
        features = [float(request.form[f]) for f in feature_names]
    except ValueError:
        return render_template('./templates/index.html')

    input_data = [features]

    # Make prediction
    pred = model.predict(input_data)

    # Display the result
    if pred[0] == 0:
        result = "Dengue is not infected"
    else:
        result = "Dengue is infected"

    return render_template('index.html', result=result)

    webview.create_window('Flask to exe',app)

if __name__ == '__main__':
    app.run(debug=True)

