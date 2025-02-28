import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class ChatClient:
    def __init__(self, host="127.0.0.1", port=5000):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.root = tk.Tk()
        self.root.title("P2P Chat")

        self.username = simpledialog.askstring("Username", "Enter your username:")
        
        # Chat display area
        self.chat_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.chat_box.pack(pady=10)
        self.chat_box.config(state=tk.DISABLED)

        # Message entry field
        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

        # Start listening for messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

        self.root.mainloop()

    def receive_messages(self):
        """Receive messages from the server and display them."""
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if not message:
                    break
                self.chat_box.config(state=tk.NORMAL)
                self.chat_box.insert(tk.END, f"\n{message}")
                self.chat_box.yview(tk.END)
                self.chat_box.config(state=tk.DISABLED)
            except:
                break

    def send_message(self):
        """Send message to the server."""
        message = self.message_entry.get()
        if message.strip():
            formatted_message = f"{self.username}: {message}"
            self.client.send(formatted_message.encode("utf-8"))
            self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    ChatClient()
