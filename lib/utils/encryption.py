from Crypto.PublicKey import ElGamal
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

class Encryption:
    def __init__(self, public_key=None, private_key=None):
        if public_key:
            self.public_key = ElGamal.import_key(public_key)
        if private_key:
            self.private_key = ElGamal.import_key(private_key)

    def encrypt_data(self, data):
        """Encrypts the provided data using the public key."""
        cipher = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher.encrypt(data.encode('utf-8'))
        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt_data(self, encrypted_data):
        """Decrypts the provided encrypted data using the private key."""
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
        return decrypted_data.decode('utf-8')

# Example usage:
# public_key = '...'  # Your public key here
# private_key = '...'  # Your private key here
# encryptor = Encryption(public_key=public_key, private_key=private_key)
# encrypted = encryptor.encrypt_data("Hello, World!")
# decrypted = encryptor.decrypt_data(encrypted)
