import socket

def start_client():
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server (running on 'localhost' at port 12345)
    client_socket.connect(('localhost', 12345))
    
    # Send a message to the server
    client_message = "Hello, Server!"
    client_socket.send(client_message.encode('utf-8'))
    
    # Receive a message from the server (maximum 1024 bytes)
    server_message = client_socket.recv(1024).decode('utf-8')
    print(f"Server says: {server_message}")
    
    # Close the connection
    client_socket.close()

# Run the client function
if __name__ == "__main__":
    start_client()
