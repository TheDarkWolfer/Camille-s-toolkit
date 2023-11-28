import socket

def main():
    server_address = ('localhost', 8080)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    
    while True:
        message = input("Enter a message to send to the server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    main()
