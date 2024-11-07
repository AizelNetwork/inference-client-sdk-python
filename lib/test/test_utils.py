# lib/test/test_utils.py

import unittest
from unittest.mock import patch, MagicMock
from lib.utils.encryption import Encryption
from lib.utils.network import get_network_config
from lib.utils.nonceManager import NonceManager

class TestUtils(unittest.TestCase):

    def test_encrypt_decrypt_data(self):
        # Sample data for encryption and decryption
        sample_data = "Hello, World!"

        # For testing purposes, generate a public/private key pair
        from Crypto.PublicKey import RSA
        key = RSA.generate(2048)
        public_key_pem = key.publickey().export_key().decode('utf-8')
        private_key_pem = key.export_key().decode('utf-8')

        # Instantiate the Encryption class with the public and private keys
        encryptor = Encryption(public_key=public_key_pem, private_key=private_key_pem)

        # Encrypt the data
        encrypted_data = encryptor.encrypt_data(sample_data)
        self.assertIsNotNone(encrypted_data)

        # Decrypt the data
        decrypted_data = encryptor.decrypt_data(encrypted_data)
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
        user_key = '35a7c90c53c351aab052953e52ec40c556bb7bff16194b38336dab4bd29c3cc8'
        network_id = 'aizel'

        # Use add_nonce to add a nonce
        nonce_manager.add_nonce(user_key, network_id, 1)

        # Retrieve the nonce
        retrieved_nonce = nonce_manager.get_nonce(user_key, network_id)
        self.assertEqual(retrieved_nonce, 1)

        # Check for a non-existent nonce
        non_existent_nonce = nonce_manager.get_nonce('non_existent_user', network_id)
        self.assertEqual(non_existent_nonce, 0)


if __name__ == '__main__':
    unittest.main()
