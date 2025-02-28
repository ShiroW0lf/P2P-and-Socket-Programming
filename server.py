import socket
import hashlib
import pickle
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class DHTClient:
    def __init__(self, host, port, username):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        
        # Peer ID generation (hash of username)
        self.peer_id = hashlib.sha256(username.encode('utf-8')).hexdigest()
        self.username = username
        
        # Join the DHT network
        self.join_network()
        
        # UI setup
        self.root = tk.Tk()
        self.root.title(f"Peer Chat - {self.username}")

        self.chat_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.chat_box.pack(pady=10)
        self.chat_box.config(state=tk.DISABLED)

        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

        threading.Thread(target=self.receive_messages, daemon=True).start()

        self.root.mainloop()

    def join_network(self):
        """Join the DHT network by sending a JOIN request."""
        join_message = {"command": "JOIN", "peer_id": self.peer_id, "peer_info": (self.username, self.client_socket.getsockname())}
        self.client_socket.send(pickle.dumps(join_message))
        
        # Wait for the server's acknowledgment
        response = self.client_socket.recv(1024)
        response = pickle.loads(response)
        print(f"Server response: {response}")

    def send_message(self):
        """Send a message to another peer."""
        message = self.message_entry.get()
        if message.strip():
            # Look up the recipient peer using their peer ID (you would normally lookup a specific peer)
            peer_id_to_lookup = hashlib.sha256("OtherUser".encode('utf-8')).hexdigest()  # Example ID
            
            lookup_message = {"command": "LOOKUP", "peer_id": peer_id_to_lookup}
            self.client_socket.send(pickle.dumps(lookup_message))
            
            response = self.client_socket.recv(1024)
            response = pickle.loads(response)
            if response["status"] == "FOUND":
                recipient_info = response["peer_info"]
                print(f"Found peer {recipient_info}")
                # You can now establish direct communication with this peer (e.g., through socket)
                # Send your message to the peer
                
            self.display_message(f"Me: {message}")
            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        """Receives messages from the server and displays them in the UI."""
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.display_message(message)
            except socket.error:
                print("Server disconnected.")
                break

    def display_message(self, message):
        """Updates chat UI with new messages."""
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, f"{message}\n")
        self.chat_box.yview(tk.END)
        self.chat_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    host = "127.0.0.1"  # IP of the DHT server
    port = 5000          # Port for the DHT server
    username = simpledialog.askstring("Username", "Enter your username:")
    DHTClient(host, port, username)
