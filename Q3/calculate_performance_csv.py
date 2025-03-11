import pandas as pd

# Load the CSV file
file_path = "./diff_vm/case4/case4_wireshark.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Define client and server IP addresses
client_ip = "192.168.64.3"
server_ip = "192.168.64.2"

# Extract relevant data
df["Length"] = df["Length"].astype(int)
df["Time"] = df["Time"].astype(float)

# Calculate total transmission time
total_time = df["Time"].iloc[-1] - df["Time"].iloc[0]

# Throughput: Total data transmitted / Total time
total_data = df["Length"].sum()  # Sum of all packet sizes
throughput = total_data / total_time  # Bytes per second

# Goodput: Only useful data (sent from client to server) / Total time
useful_data = df[(df["Source"] == client_ip) & (df["Destination"] == server_ip)]["Length"].sum()
goodput = useful_data / total_time  # Bytes per second

# Packet loss rate: Sent packets that were not acknowledged
sent_packets = df[df["Source"] == client_ip].shape[0]
received_packets = df[df["Destination"] == client_ip].shape[0]
packet_loss_rate = (sent_packets - received_packets) / sent_packets * 100 if sent_packets > 0 else 0

# Maximum packet size achieved
max_packet_size = df["Length"].max()

# Print results
print(f"Throughput: {throughput:.2f} bytes/s")
print(f"Goodput: {goodput:.2f} bytes/s")
print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")
print(f"Maximum Packet Size: {max_packet_size} bytes")
