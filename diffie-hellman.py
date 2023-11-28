from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate Alice's private and public keys
alice_parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
alice_private_key = alice_parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()

# Serialize Alice's public key to share with Bob
alice_public_key_bytes = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generate Bob's private and public keys using the same parameters
bob_private_key = alice_parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

# Serialize Bob's public key to share with Alice
bob_public_key_bytes = bob_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# In a real implementation, Alice and Bob would exchange public keys at this point

# Alice and Bob calculate the shared secret
alice_shared_key = alice_private_key.exchange(bob_public_key)
bob_shared_key = bob_private_key.exchange(alice_public_key)

# The shared keys should be the same
if alice_shared_key == bob_shared_key:
    print("Shared keys match!")
else:
    print("Shared keys do not match!")

# You can use the shared key as a symmetric encryption key for further communication.

#######################################################################
###############SERVER SIDE#############################################
#######################################################################

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh

# Server generates private and public keys
def generate_server_keys():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Serialize the server's public key to send to the client
def serialize_server_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

# Calculate the shared secret using the client's public key
def calculate_shared_secret(server_private_key, client_public_key):
    shared_secret = server_private_key.exchange(client_public_key)
    return shared_secret

#######################################################################
###############END SERVER SIDE#########################################
#######################################################################

#######################################################################
###############CLIENT SIDE#############################################
#######################################################################
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh

# Client generates private and public keys
def generate_client_keys():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Serialize the client's public key to send to the server
def serialize_client_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

# Calculate the shared secret using the server's public key
def calculate_shared_secret(client_private_key, server_public_key):
    shared_secret = client_private_key.exchange(server_public_key)
    return shared_secret

#######################################################################
###############END CLIENT SIDE#########################################
#######################################################################