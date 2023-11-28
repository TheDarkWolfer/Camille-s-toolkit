import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"Connection closed by {address}")
            break
        message = data.decode()
        print(f"Received from {address}: {message}")
        client_socket.send(data)
    
    client_socket.close()

def main():
    server_address = ('localhost', 8080)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server is listening...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()