from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class Encryption:
    def __init__(self, public_key=None, private_key=None):
        if public_key:
            self.public_key = RSA.import_key(public_key)
        if private_key:
            self.private_key = RSA.import_key(private_key)

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
