import pytest
import requests
from bs4 import BeautifulSoup

# Define the URL of your Flask application
BASE_URL = 'http://127.0.0.1:5000'

# Sample input data for testing
SAMPLE_INPUT_DATA = {
    '0': '1', '1': '0', '2': '0'
}

def test_predict_route():
    # Send a POST request to the predict route with sample input data
    response = requests.post(f'{BASE_URL}/dengueprediction', data=SAMPLE_INPUT_DATA)

    print(response.content)

    # Check if the response is successful (status code 500)
    assert response.status_code == 200
    
    # Parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the result
    result_element = soup.find(id='resultMessage')
    
    # Extract the result text
    result = result_element.get_text() if result_element else None
    
    # Check if the expected messages are present in the result
    assert 'Dengue is infected' in result or 'Dengue is not infected' in result

if __name__ == "__main__":
    pytest.main()
