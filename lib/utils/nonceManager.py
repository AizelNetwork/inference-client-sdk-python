from collections import defaultdict

class NonceManager:
    def __init__(self):
        # A dictionary to hold nonces for each user and network
        self.nonces = defaultdict(lambda: defaultdict(int))

    def add_nonce(self, user_address, network_id, nonce=1):
        """Adds a specific nonce value for a user on a network."""
        self.nonces[network_id][user_address] += nonce

    def get_nonce(self, user_address, network_id):
        """Returns the current nonce for the given user and network, then increments it."""
        current_nonce = self.nonces[network_id][user_address]
        self.nonces[network_id][user_address] += 1  # Increment the nonce for the next use
        return current_nonce

    def reset_nonce(self, user_address, network_id):
        """Resets the nonce for the given user and network."""
        self.nonces[network_id][user_address] = 0

    def set_nonce(self, user_address, network_id, nonce):
        """Sets the nonce for the given user and network to a specific value."""
        self.nonces[network_id][user_address] = nonce
