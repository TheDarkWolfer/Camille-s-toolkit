import hashlib
import os
from cryptography.fernet import Fernet

def generate_encryption_key(passphrase, salt=None, iterations=100000, key_length=32):
    if not salt:
        salt = os.urandom(16)  # Generate a random salt
    
    key = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), salt, iterations, dklen=key_length)
    return salt, key

def encrypt_text(text, encryption_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, encryption_key):
    cipher_suite = Fernet(encryption_key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text