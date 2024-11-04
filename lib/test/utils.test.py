import unittest
from unittest.mock import patch, MagicMock
from lib.utils.encryption import encrypt_data, decrypt_data
from lib.utils.network import get_network_config
from lib.utils.nonceManager import NonceManager

class TestUtils(unittest.TestCase):

    def test_encrypt_decrypt_data(self):
        # Sample data for encryption and decryption
        sample_data = "Hello, World!"
        key = "test_key"  # Use an appropriate key for your encryption method

        # Encrypt the data
        encrypted_data = encrypt_data(sample_data, key)
        self.assertIsNotNone(encrypted_data)

        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data, key)
        self.assertEqual(decrypted_data, sample_data)

    @patch('lib.utils.network.requests.get')
    def test_get_network_config(self, mock_get):
        # Mock the response from the GET request
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "network_name": "aizel",
            "evm_chain_id": 1281,
            "rpc_url": "http://34.124.144.235:9946",
            "contracts": {
                "INFERENCE": "0x313bE302AB078e3207f74559d63eF316c0B0670D"
            }
        }
        mock_get.return_value = mock_response

        # Call the method
        network_config = get_network_config('aizel')

        # Check the response
        self.assertEqual(network_config['network_name'], 'aizel')
        self.assertEqual(network_config['evm_chain_id'], 1281)
        self.assertEqual(network_config['rpc_url'], 'http://34.124.144.235:9946')
        self.assertIn('INFERENCE', network_config['contracts'])

    def test_nonce_manager(self):
        # Create an instance of NonceManager
        nonce_manager = NonceManager()

        # Add a nonce for a user
        user_key = 'test_user'
        nonce_manager.add_nonce(user_key, 1)

        # Retrieve the nonce
        retrieved_nonce = nonce_manager.get_nonce(user_key)
        self.assertEqual(retrieved_nonce, 1)

        # Check for a non-existent nonce
        non_existent_nonce = nonce_manager.get_nonce('non_existent_user')
        self.assertIsNone(non_existent_nonce)

if __name__ == '__main__':
    unittest.main()
