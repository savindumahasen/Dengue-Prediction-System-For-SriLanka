import pytest
import requests

# Define the URL of your Flask application
BASE_URL = 'http://127.0.0.1:5000'

# Sample input data for testing
SAMPLE_INPUT_DATA = {
       '0': '0', '1': '0', '2': '0', '3': '0', '4':'1', '5':'1', '6':'1','7':'1','8':'1'
}

def test_predict_route():
    # Send a POST request to the predict route with sample input data
    response = requests.post(f'{BASE_URL}/dengueprediction', data=SAMPLE_INPUT_DATA)
    
    # Check if the response is successful (status code 200)
    assert response.status_code == 200
   
if __name__ == "__main__":
    pytest.main()
