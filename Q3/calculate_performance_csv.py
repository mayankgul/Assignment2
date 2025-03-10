import pandas as pd

# Load the CSV file (update the filename)
csv_file = "./case4/case4_wireshark.csv"  # Change this to your actual file path
df = pd.read_csv(csv_file)

# Convert 'Time' and 'Length' columns to proper data types
df["Time"] = df["Time"].astype(float)
df["Length"] = df["Length"].astype(int)

# Compute total duration (last timestamp - first timestamp)
total_time = df["Time"].max() - df["Time"].min()

# Sum up all packet lengths (in bytes) and convert to bits
total_bytes = df["Length"].sum()
total_bits = total_bytes * 8

# Calculate throughput (bits per second)
throughput = total_bits / total_time

# Identify application-level data packets (assuming [PSH, ACK] carries useful data)
goodput_packets = df[df["Info"].str.contains("PSH, ACK", na=False)]
goodput_bytes = goodput_packets["Length"].sum()
goodput_bits = goodput_bytes * 8

# Calculate goodput (bits per second)
goodput = goodput_bits / total_time

# Estimate packet loss (by checking for retransmissions)
total_packets_sent = len(df)  # Total number of packets
retransmissions = df[df["Info"].str.contains("Retransmission", na=False)]  # Retransmitted packets
lost_packets = len(retransmissions)  # Assuming retransmissions indicate loss
packet_loss_rate = (lost_packets / total_packets_sent) * 100 if total_packets_sent > 0 else 0

# Find maximum packet size
max_packet_size = df["Length"].max()

# Print results
print(f"Total Data Transferred: {total_bytes} bytes ({total_bits} bits)")
print(f"Total Time: {total_time:.6f} seconds")
print(f"Throughput: {throughput:.2f} bps")
print(f"Goodput: {goodput:.2f} bps")
print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")
print(f"Maximum Packet Size: {max_packet_size} bytes")