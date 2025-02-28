# Peer-to-Peer Chat Application

## Overview
This is a simple Peer-to-Peer (P2P) chat application that allows two users to communicate over a network using sockets. One user acts as the host, while the other joins as a peer.

## Features
- Host a chat session and wait for a peer to connect.
- Join an existing chat session using the host's IP address.
- Modern, user-friendly graphical interface (GUI) using Tkinter.
- Real-time message exchange between peers.

## Prerequisites
Ensure you have Python installed on your system.
- Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation
1. Clone or download the repository to your local machine.
2. Install dependencies (if any, but Tkinter is built into Python by default).

## How to Run
### Hosting a Chat
1. Run the `ChatAppHost.py` script:
   ```sh
   python ChatAppHost.py
   ```
2. Click the "Host Chat" button.
3. The application will start a server and wait for a peer to connect.
4. **Find Your IP Address:**
   - Windows: Open Command Prompt and type:
     ```sh
     ipconfig
     ```
     Look for the `IPv4 Address` under your active network adapter.
   - macOS/Linux: Open Terminal and type:
     ```sh
     ifconfig
     ```
     or
     ```sh
     hostname -I
     ```
   - Share this IP address with the peer who wants to join.

### Joining a Chat
1. Run the `ChatAppPeer.py` script:
   ```sh
   python ChatAppPeer.py
   ```
2. Click the "Join Chat" button.
3. Enter the **host's IP address** when prompted.
4. If the connection is successful, you will be able to chat in real time!

## Troubleshooting
- **Connection issues?**
  - Ensure both devices are on the same network.
  - Check if a firewall is blocking the connection.
  - Verify that the correct IP address is used.
- **Chat window not appearing?**
  - Ensure the script runs with Python 3.
- **Messages not sending?**
  - Make sure a peer is connected before sending messages.

## Future Enhancements
- Support for multiple peers.
- Implementing encryption for secure messaging.

Enjoy chatting! 🎉

--

### ✅ **Initial Requirements vs. This Implementation**  

| Requirement | Implemented? | Notes |
|-------------|-------------|--------|
| **Peer-to-Peer Communication** | ✅ Yes | Users can host or join a chat directly. |
| **Socket-based Communication** | ✅ Yes | Uses Python’s `socket` module for TCP-based messaging. |
| **GUI with Tkinter** | ✅ Yes | Clean, modern interface built with Tkinter. |
| **Sending & Receiving Messages** | ✅ Yes | Messages are sent over sockets and displayed in the UI. |
| **Host/Join Mechanism** | ✅ Yes | A welcome screen lets users choose to **host** or **join** a chat. |
| **Message Input Field** | ✅ Yes | Users can type and send messages with **Enter key support**. |
| **Scrollable Chat Window** | ✅ Yes | Uses `scrolledtext.ScrolledText` for a better chat experience. |
| **Automatic Message Display** | ✅ Yes | New messages appear automatically, with **auto-scrolling**. |
| **Connection Status Display** | ✅ Yes | Status updates dynamically when a peer connects/disconnects. |
| **Error Handling** | ✅ Yes | Alerts for connection failures & auto-recovery. |
| **Graceful Exit** | ✅ Yes | Closes sockets properly when the app shuts down. |

---

### **💡 What’s Improved Beyond the Minimum Requirements?**
🚀 **Modern UI with Dark Mode** – Clean, Discord-like theme.  
🚀 **Welcome Screen for Better UX** – Reduces confusion when starting.  
🚀 **Connection Errors are Handled Gracefully** – No crashes on failed connections.  
🚀 **Enter Key to Send Messages** – More intuitive than clicking "Send" every time.  
🚀 **Live Connection Status Updates** – Always know if you're connected.  
🚀 **Auto-Scrolling Messages** – No need to scroll manually.  

---

### **🔍 What's Missing? (Extra Credit Features)**
❌ **File Transfer** – Not included yet.  
❌ **Multiple Clients in One Chat** – Currently only supports **1:1 chat**.  
❌ **Encryption for Messages** – Not implemented.  


