# Peer-to-Peer Chat Application

## Overview
This is a simple Peer-to-Peer (P2P) chat application utilizing a Distributed Hash Table (DHT) for peer lookup and message routing. One user acts as the host, while the other joins as a peer without a central server.
## Features
- Host a chat session and wait for a peer to connect using a DHT network.
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



