# Chat Application

## Overview
This is a peer-to-peer group chat application that allows users to either host a chat session or join an existing one. The application is built using Python with a graphical user interface (GUI) created in Tkinter. It supports multiple clients and enables seamless real-time communication.

## Features
- Host a chat session and allow multiple clients to join
- Join an existing chat session by entering the host's IP address
- Modern and user-friendly UI with a dark theme
- Scrollable chat display with automatic updates
- Message broadcasting for group communication
- Graceful handling of disconnections and errors
- Supports sending messages using the Enter key

## Prerequisites
- Python 3.x

## Installation
1. Clone this repository or download the script files:
   ```sh
   git clone <repository-url>
   ```
2. Install the required dependencies (Tkinter comes pre-installed with Python):
   ```sh
   pip install tk
   ```

## How to Run
The application consists of a single script (`GroupChat.py`). It can be run in two different modes:

### Hosting a Chat Session
1. Run the script:
   ```sh
   python GroupChat.py
   ```
2. Enter a username and click on "Host a Chat."
3. The server will start listening for connections. Your system's local IP address is required for peers to join.
4. To find your IP address:
   - On Windows: Open Command Prompt and type:
     ```sh
     ipconfig
     ```
     Look for `IPv4 Address` under your network adapter.
   - On macOS/Linux: Open Terminal and type:
     ```sh
     ifconfig
     ```
     or
     ```sh
     hostname -I
     ```
5. Share this IP address with peers so they can connect.

### Joining a Chat Session
1. Run the script:
   ```sh
   python GroupChat.py
   ```
2. Enter a username and click on "Join a Chat."
3. Enter the host's IP address when prompted.
4. If the connection is successful, you can start chatting with the group.

## Usage
- Type a message in the text entry box and press **Enter** or click **Send** to broadcast the message to all connected peers.
- The chat history will be displayed in a scrollable text box.
- The status label at the bottom indicates the connection status.
- The application will handle disconnections and update the UI accordingly.

## Technical Details
- The host acts as a server, accepting multiple client connections.
- The server maintains a list of connected clients and forwards messages to all participants.
- The client establishes a TCP connection with the host and receives messages in a separate thread to keep the UI responsive.
- Error handling is implemented to manage connection failures and unexpected disconnections.

## Exit Strategy
- The application can be closed using the window's close button.
- The `on_closing` function ensures proper cleanup by closing all active sockets before exiting.

## Future Enhancements
- Adding file-sharing capabilities.
- Enhancing security with encryption.
- Implementing a GUI-based IP address detection feature.

## Credits
Developed by [Your Name].

