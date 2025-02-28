import socket
import threading

clients = []  # Store connected clients

def broadcast(message, sender_socket):
    """Send message to all clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    """Handle incoming messages from a client."""
    print(f"New connection: {addr}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break
    print(f"Client {addr} disconnected")
    clients.remove(client_socket)
    client_socket.close()

def start_server(host="127.0.0.1", port=5050):
    """Start the chat server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server running on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
