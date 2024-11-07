# lib/test/test_InferenceClient.py

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Add the 'lib' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib')))

import InferenceClient  # Import InferenceClient as a module

class TestInferenceClient(unittest.TestCase):

    def setUp(self):
        self.client = InferenceClient.InferenceClient(
            base_url='http://34.124.144.235:8080/api',
            app_key='35a7c90c53c351aab052953e52ec40c556bb7bff16194b38336dab4bd29c3cc8'
        )

    @patch('InferenceClient.requests.post')
    def test_launch_inference(self, mock_post):
        # Mock the response from the POST request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'requestId': '12345',
            'status': 'success'
        }
        mock_post.return_value = mock_response

        # Call the method
        response = self.client.launch_inference(user_input='test input', model_id='test_model')

        # Check the response
        self.assertEqual(response['requestId'], '12345')
        self.assertEqual(response['status'], 'success')
        mock_post.assert_called_once()

    @patch('InferenceClient.requests.post')
    def test_get_inference_output(self, mock_post):
    # Mock the response from the POST request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'result': 'Inference result'
        }
        mock_post.return_value = mock_response

        # Call the method with the correct name
        response = self.client.get_inference_output(request_id='12345')

        # Check the response
        self.assertEqual(response['result'], 'Inference result')
        mock_post.assert_called_once()


if __name__ == '__main__':
    unittest.main()
