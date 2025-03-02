import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import simpledialog


# Custom Colors and Styling
BG_COLOR = "#2C2F33"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#7289DA"
ENTRY_BG = "#23272A"
FONT = ("Arial", 12)

class GroupChat:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Group Chat")
        self.root.geometry("500x500")
        self.root.configure(bg=BG_COLOR)

        self.clients = []  # Only used by the host
        self.username = ""
        
        # Welcome Screen
        self.welcome_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.welcome_frame.pack(expand=True, fill="both")

        tk.Label(self.welcome_frame, text="Group Chat", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)
        
        tk.Label(self.welcome_frame, text="Enter Username:", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR).pack()
        self.username_entry = tk.Entry(self.welcome_frame, width=30, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT)
        self.username_entry.pack(pady=5)
        
        tk.Button(self.welcome_frame, text="Host a Chat", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.host_mode).pack(pady=10)
        tk.Button(self.welcome_frame, text="Join a Chat", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.client_mode).pack(pady=10)

        # Chat Screen
        self.chat_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.chat_box = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=60, height=20, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT)
        self.chat_box.pack(pady=10, padx=10)
        self.chat_box.config(state=tk.DISABLED)
        
        self.message_entry = tk.Entry(self.chat_frame, width=40, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT)
        self.message_entry.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill="x")
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.chat_frame, text="Send", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        self.status_label = tk.Label(self.chat_frame, text="Not Connected", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR)
        self.status_label.pack(pady=5)

        self.server = None
        self.conn = None
        self.running = True

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def switch_to_chat_ui(self, status):
        self.username = self.username_entry.get().strip() or "Guest"
        self.welcome_frame.pack_forget()
        self.chat_frame.pack(expand=True, fill="both")
        self.status_label.config(text=status)

    def host_mode(self):
        self.switch_to_chat_ui("Hosting... Waiting for connections.")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 5000))
        self.server.listen(5)
        self.display_message("[INFO] Waiting for peers to connect...")
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while self.running:
            conn, addr = self.server.accept()
            self.clients.append(conn)
            threading.Thread(target=self.receive_messages, args=(conn,), daemon=True).start()
            self.display_message(f"[INFO] {addr} connected.")

    def client_mode(self):
        self.switch_to_chat_ui("Connecting...")
        peer_ip = tk.simpledialog.askstring("Peer IP", "Enter the host's IP address:")
        if not peer_ip:
            return
        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.connect((peer_ip, 5000))
            self.status_label.config(text=f"Connected to {peer_ip}")
            self.display_message(f"[INFO] Connected to {peer_ip}")
            threading.Thread(target=self.receive_messages, args=(self.conn,), daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Failed", f"Could not connect: {e}")

    def receive_messages(self, conn):
        while self.running:
            try:
                message = conn.recv(1024).decode("utf-8")
                if not message:
                    break
                self.display_message(message)
            except:
                self.display_message("[ERROR] Connection lost.")
                self.status_label.config(text="Disconnected")
                break

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message.strip():
            formatted_message = f"{self.username}: {message}"
            self.display_message(formatted_message)
            self.message_entry.delete(0, tk.END)
            self.broadcast_message(formatted_message)

    def broadcast_message(self, message):
        if self.server:
            for client in self.clients:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    self.clients.remove(client)
        elif self.conn:
            try:
                self.conn.send(message.encode("utf-8"))
            except:
                self.display_message("[ERROR] Message sending failed.")

    def display_message(self, message):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, f"{message}\n")
        self.chat_box.yview(tk.END)
        self.chat_box.config(state=tk.DISABLED)

    def on_closing(self):
        self.running = False
        if self.conn:
            self.conn.close()
        if self.server:
            self.server.close()
        self.root.destroy()

if __name__ == "__main__":
    GroupChat()
