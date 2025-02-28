import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

# Custom Colors and Styling
BG_COLOR = "#2C2F33"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#7289DA"
ENTRY_BG = "#23272A"
FONT = ("Arial", 12)

class PeerChat:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Peer-to-Peer Chat")
        self.root.geometry("500x500")
        self.root.configure(bg=BG_COLOR)

        # === Welcome Screen ===
        self.welcome_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.welcome_frame.pack(expand=True, fill="both")

        tk.Label(self.welcome_frame, text="Peer-to-Peer Chat", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=20)
        tk.Button(self.welcome_frame, text="Host a Chat", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.host_mode).pack(pady=10)
        tk.Button(self.welcome_frame, text="Join a Chat", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.client_mode).pack(pady=10)

        # === Chat Screen ===
        self.chat_frame = tk.Frame(self.root, bg=BG_COLOR)

        # Chat Display
        self.chat_box = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=60, height=20, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT)
        self.chat_box.pack(pady=10, padx=10)
        self.chat_box.config(state=tk.DISABLED)

        # Message Input
        self.message_entry = tk.Entry(self.chat_frame, width=40, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT)
        self.message_entry.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill="x")
        self.message_entry.bind("<Return>", self.send_message)

        # Send Button
        self.send_button = tk.Button(self.chat_frame, text="Send", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        # Connection Status
        self.status_label = tk.Label(self.chat_frame, text="Not Connected", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR)
        self.status_label.pack(pady=5)

        # Connection attributes
        self.server = None
        self.conn = None
        self.running = True

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window closing
        self.root.mainloop()

    def switch_to_chat_ui(self, status):
        """Switches from the welcome screen to the chat UI with a status message."""
        self.welcome_frame.pack_forget()
        self.chat_frame.pack(expand=True, fill="both")
        self.status_label.config(text=status)

    def host_mode(self):
        """Starts the chat server."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 5000))
        self.server.listen(1)

        self.switch_to_chat_ui("Hosting... Waiting for connection.")
        self.display_message("[INFO] Waiting for a peer to connect...")

        threading.Thread(target=self.accept_connection, daemon=True).start()

    def accept_connection(self):
        """Accepts an incoming connection from a client."""
        self.conn, addr = self.server.accept()
        self.display_message(f"[INFO] Connected with {addr}")
        self.status_label.config(text=f"Connected to {addr[0]}")
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def client_mode(self):
        """Attempts to connect to a host."""
        peer_ip = simpledialog.askstring("Peer IP", "Enter the host's IP address:")
        if not peer_ip:
            return

        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.connect((peer_ip, 5000))
            self.switch_to_chat_ui(f"Connected to {peer_ip}")
            self.display_message(f"[INFO] Connected to {peer_ip}")
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Failed", f"Could not connect: {e}")
            self.display_message("[ERROR] Connection failed.")

    def receive_messages(self):
        """Receives messages from the peer and updates UI."""
        while self.running:
            try:
                message = self.conn.recv(1024).decode("utf-8")
                if not message:
                    break
                self.display_message(message)
            except Exception:
                self.display_message("[ERROR] Connection lost.")
                self.status_label.config(text="Disconnected")
                break

    def send_message(self, event=None):
        """Sends a message to the connected peer."""
        message = self.message_entry.get()
        if message.strip() and self.conn:
            try:
                self.conn.send(message.encode("utf-8"))
                self.display_message(f"You: {message}")
                self.message_entry.delete(0, tk.END)
            except Exception as e:
                self.display_message(f"[ERROR] Message sending failed: {e}")
        else:
            self.display_message("[ERROR] No active connection!")

    def display_message(self, message):
        """Updates the chat UI with new messages."""
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, f"{message}\n")
        self.chat_box.yview(tk.END)
        self.chat_box.config(state=tk.DISABLED)

    def on_closing(self):
        """Handles cleanup when the window is closed."""
        self.running = False
        if self.conn:
            self.conn.close()
        if self.server:
            self.server.close()
        self.root.destroy()


if __name__ == "__main__":
    PeerChat()
