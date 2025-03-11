from scapy.all import rdpcap
import matplotlib.pyplot as plt
from scapy.layers.inet import IP, TCP

conn_tracker = {}
pcap_data = rdpcap('Q2-part2.pcap')
for pkt in pcap_data:
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        ip_hdr = pkt[IP]
        tcp_hdr = pkt[TCP]
        conn_id = (ip_hdr.src, ip_hdr.dst, tcp_hdr.sport, tcp_hdr.dport)
        reverse_id = (ip_hdr.dst, ip_hdr.src, tcp_hdr.dport, tcp_hdr.sport)
        if tcp_hdr.flags & 0x02 and not tcp_hdr.flags & 0x10: 
            if conn_id not in conn_tracker:
                conn_tracker[conn_id] = {'start': pkt.time, 'end': None, 'status': 'active'}
        elif tcp_hdr.flags & 0x01 or tcp_hdr.flags & 0x04:  
            if reverse_id in conn_tracker and conn_tracker[reverse_id]['status'] == 'active':
                conn_tracker[reverse_id]['end'] = pkt.time
                conn_tracker[reverse_id]['status'] = 'closed'

start_timestamps = []
conn_durations = []
base_time = min(entry['start'] for entry in conn_tracker.values())
for conn in conn_tracker.values():
    start_timestamps.append(conn['start'] - base_time)
    conn_durations.append((conn['end'] - conn['start']) if conn['end'] else 100)

plt.figure(figsize=(12, 6))
plt.scatter(start_timestamps, conn_durations, alpha=0.6, color='green', label='Connection time')
plt.axvline(x=20, color='yellow', linestyle='--', label='start attack (20s)')
plt.axvline(x=120, color='orange', linestyle='--', label='end attack (120s)')
plt.xlabel(' Start connection Time (sec)')
plt.ylabel('Connection time (sec)')
plt.title('SYN Flood Attack: Connection time vs. Start Time')
plt.legend()
plt.grid(True)
plt.savefig("connection_duration_plot.png")
