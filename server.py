import socket
import threading

clients = []  # List to store connected clients

def handle_client(client_socket, username):
    """Handles receiving messages from a client and broadcasting to all other clients."""
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break

    print(f"[INFO] {username} disconnected.")
    clients.remove((client_socket, username))
    broadcast(f"[INFO] {username} has left the chat.", client_socket)
    client_socket.close()

def broadcast(message, sender_socket=None):
    """Sends a message to all connected clients except the sender."""
    print(f"Broadcasting: {message}")
    for client_socket, _ in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except:
                clients.remove((client_socket, _))

def start_server(host="127.0.0.1", port=5000):
    """Starts the chat server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[INFO] Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[NEW CONNECTION] {addr}")

        client_socket.send("USERNAME_REQUEST".encode("utf-8"))
        username = client_socket.recv(1024).decode("utf-8")
        clients.append((client_socket, username))

        print(f"[INFO] {username} joined the chat.")
        broadcast(f"[INFO] {username} joined the chat.", client_socket)

        # Start handling client in a separate thread
        threading.Thread(target=handle_client, args=(client_socket, username), daemon=True).start()

if __name__ == "__main__":
    start_server()
