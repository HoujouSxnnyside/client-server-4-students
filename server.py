import socket

def start_server():
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to an address and port
    server_socket.bind(('localhost', 12345))
    
    # Start listening for incoming connections (1 means the server will allow 1 connection at a time)
    server_socket.listen(1)
    print("Server started, waiting for connections...")
    
    # Accept a connection from a client
    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")
    
    # Receive data from the client (maximum 1024 bytes)
    client_message = conn.recv(1024).decode('utf-8')
    print(f"Client says: {client_message}")
    
    # Send a message back to the client
    server_message = "Hello, Client! Message received."
    conn.send(server_message.encode('utf-8'))
    
    # Close the connection
    conn.close()
    print("Connection closed.")

# Run the server function
if __name__ == "__main__":
    start_server()
