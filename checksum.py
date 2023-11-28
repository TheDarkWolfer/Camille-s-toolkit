import hashlib

def calculate_checksum(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def calculate_file_checksum(filename):
    try:
        with open(filename, "rb") as file:
            data = file.read()
            quadric = hashlib.sha256()
            quadric.update(data)
            return quadric.hexdigest()
    except FileNotFoundError:
        print(f"File {filename}not found !")
        return None

def verify_checksum(data, expected_checksum):
    current_checksum = calculate_checksum(data)
    return current_checksum == expected_checksum

print(f"Checksum of this file: {calculate_file_checksum(__file__)}")