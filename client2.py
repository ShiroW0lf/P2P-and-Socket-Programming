import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class ChatClient:
    def __init__(self, host="127.0.0.1", port=5000):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        # Request username from server
        server_message = self.client.recv(1024).decode("utf-8")
        if server_message == "USERNAME_REQUEST":
            self.username = simpledialog.askstring("Username", "Enter your username:")
            self.client.send(self.username.encode("utf-8"))

        # UI setup
        self.root = tk.Tk()
        self.root.title(f"Chat - {self.username}")

        self.chat_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.chat_box.pack(pady=10)
        self.chat_box.config(state=tk.DISABLED)

        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

        threading.Thread(target=self.receive_messages, daemon=True).start()

        self.root.mainloop()

    def receive_messages(self):
        """Receives messages from the server and displays them in the UI."""
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if not message:
                    print("[DEBUG] Server disconnected.")
                    break
                self.display_message(message)  # Display message from server
            except socket.error as e:
                print(f"[ERROR] Receiving failed: {e}")
                break

    def send_message(self):
        """Sends a message to the server and updates UI."""
        message = self.message_entry.get()
        if message.strip():
            formatted_message = f"{self.username}: {message}"
            try:
                self.client.send(formatted_message.encode("utf-8"))  # Send formatted message
                self.display_message(formatted_message)  # Show message in UI immediately
                self.message_entry.delete(0, tk.END)
            except socket.error as e:
                print(f"[ERROR] Connection lost: {e}")
                self.display_message("\n[ERROR] Connection lost. Restart the client.")
                self.client.close()

    def display_message(self, message):
        """Updates chat UI with new messages."""
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, f"{message}\n")
        self.chat_box.yview(tk.END)
        self.chat_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    ChatClient()
