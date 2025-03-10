import socket
import time

SERVER_IP = '127.0.0.1'  # Change to server IP if running on separate machines
PORT = 5000
NAGLE_ALGORITHM = True

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set Nagle’s Algorithm (Enable/Disable based on test case)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 0 if NAGLE_ALGORITHM else 1)  # 0 = Enabled, 1 = Disabled

client_socket.connect((SERVER_IP, PORT))
print("Connected to server.")

# Read file and send in 40-byte chunks
with open("4KB_file.txt", "rb") as f:
    data = f.read(40)
    while data:
        client_socket.sendall(data)
        time.sleep(1)  # Send at 40 bytes/sec
        data = f.read(40)

client_socket.close()
print("File sent successfully.")
