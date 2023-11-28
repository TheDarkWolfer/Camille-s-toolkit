from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a new Fernet key and return it as a string.
    """
    key = Fernet.generate_key()
    return key

def save_key_to_file(key, filename):
    """
    Save a Fernet key to a file.
    """
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key_from_file(filename):
    """
    Load a Fernet key from a file and return it as bytes.
    """
    with open(filename, "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_string(message, key):
    """
    Encrypt a string using the provided Fernet key.
    """
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_string(encrypted_message, key):
    """
    Decrypt an encrypted string using the provided Fernet key.
    """
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

def encrypt_file(filename, key):
    """
    Encrypt a file using the provided Fernet key.
    """
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    """
    Decrypt a file using the provided Fernet key.
    """
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)