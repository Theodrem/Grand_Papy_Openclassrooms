import pytest
from app import app
from app.view import process
import json

class TestView:
    """
    This class test the views.
    """
    def test_index(self):
        """
        Check if the status of response is ok.
        """
        with app.test_client() as c:
            response = c.get('/')
            assert response.status_code == 200
            
    def test_process(self):
        with process as c:
            rv = c.post('/process', json={'input_user': "parsed_input", 'lat': "lat", 'lng': "lng",  # Return all data with json format
                    'address': "address", "message": "message",
                    'end_mess': "end_message", 'wiki': "mess_wiki"})
            
            json_data = rv.get_json()
            assert verify_token(email, json_data['token'])

