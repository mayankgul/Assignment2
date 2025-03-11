import pandas as pd

file_path = "./diff_vm/case4/case4_wireshark.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

client_ip = "192.168.64.3"
server_ip = "192.168.64.2"

df["Length"] = df["Length"].astype(int)
df["Time"] = df["Time"].astype(float)

total_time = df["Time"].iloc[-1] - df["Time"].iloc[0]

total_data = df["Length"].sum()
throughput = total_data / total_time

useful_data = df[(df["Source"] == client_ip) & (df["Destination"] == server_ip)]["Length"].sum()
goodput = useful_data / total_time


sent_packets = df[df["Source"] == client_ip].shape[0]
received_packets = df[df["Destination"] == client_ip].shape[0]
packet_loss_rate = (sent_packets - received_packets) / sent_packets * 100 if sent_packets > 0 else 0

max_packet_size = df["Length"].max()

print(f"Throughput: {throughput:.2f} bytes/s")
print(f"Goodput: {goodput:.2f} bytes/s")
print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")
print(f"Maximum Packet Size: {max_packet_size} bytes")
