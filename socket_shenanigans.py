import socket

def connect_to(REMOTE_HOST = '0.0.0.0',REMOTE_PORT = 8081):
    global client
    client = socket.socket()
    print("[-] Connection Initiating...")
    client.connect((REMOTE_HOST, REMOTE_PORT))
    print("[-] Connection initiated!")

def await_connection(HOST='0.0.0.0.0',PORT=8081):
    global client, server
    server = socket.socket()
    server.bind((HOST, PORT))
    print('[+] Server Started')
    print('[+] Listening For Client Connection ...')
    server.listen(1)
    client, client_addr = server.accept()
    print(f'[+] {client_addr} Client connected to the server')