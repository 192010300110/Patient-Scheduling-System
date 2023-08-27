## encryption.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class Encryption:
    def __init__(self, key: str):
        self.key = key

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts the given data using AES encryption.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data.
        """
        cipher = AES.new(self.key.encode(), AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
        return encrypted_data.hex()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypts the given encrypted data using AES decryption.

        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            str: The decrypted data.
        """
        cipher = AES.new(self.key.encode(), AES.MODE_CBC)
        decrypted_data = cipher.decrypt(bytes.fromhex(encrypted_data))
        return unpad(decrypted_data, AES.block_size).decode()
