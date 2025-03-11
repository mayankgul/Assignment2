import socket
import time

SERVER_IP = '192.168.64.2'
PORT = 5000
NAGLE_ALGORITHM = True

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 0 if NAGLE_ALGORITHM else 1)  # 0 = Enabled, 1 = Disabled

client_socket.connect((SERVER_IP, PORT))
print("Connected to server.")

with open("4KB_file.txt", "rb") as f:
    data = f.read(40)
    while data:
        client_socket.sendall(data)
        time.sleep(1)
        data = f.read(40)

client_socket.close()
print("File sent successfully.")
