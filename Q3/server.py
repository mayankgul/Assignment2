import socket
import time

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5000
DELAYED_ACK = True

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set Delayed-ACK (Enable/Disable based on test case)
server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 0 if DELAYED_ACK else 1)  # 0 = Enabled, 1 = Disabled

server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is listening...")

conn, address = server_socket.accept()
print(f"Connection established with {address}")

start_time = time.time()
received_data = b""

# Run for 120 seconds
while time.time() - start_time < 120:
    data = conn.recv(1024)
    if not data:
        break
    received_data += data
    # time.sleep(0.1)  # Simulate processing delay

conn.close()

# Save received data to file
with open("received_file.txt", "wb") as f:
    f.write(received_data)

print("File received successfully.")
server_socket.close()
