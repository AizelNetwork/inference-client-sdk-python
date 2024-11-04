import unittest
from unittest.mock import patch, MagicMock
from lib.InferenceClient import InferenceClient

class TestInferenceClient(unittest.TestCase):

    def setUp(self):
        self.client = InferenceClient(app_key='test_app_key')

    @patch('lib.InferenceClient.requests.post')
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

    @patch('lib.InferenceClient.requests.get')
    def test_get_output(self, mock_get):
        # Mock the response from the GET request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'result': 'Inference result'
        }
        mock_get.return_value = mock_response

        # Call the method
        response = self.client.get_output(request_id='12345')

        # Check the response
        self.assertEqual(response['result'], 'Inference result')
        mock_get.assert_called_once_with('http://34.124.144.235:8080/api/v1/inferences/output', 
                                          headers={'Authorization': 'Bearer test_app_key'})

if __name__ == '__main__':
    unittest.main()
