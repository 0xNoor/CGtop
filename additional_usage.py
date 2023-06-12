import time
import os
import subprocess
try:
	import psutil;
except:
	print("psutil not installed");

memory_usage_all = psutil.virtual_memory()

class memory:

	def __init__(self, mem):
		self.mem = mem

p = memory(memory_usage_all[1])
print(p.mem)

disk_counters = psutil.disk_io_counters()
print("Disk Counters:")
print(f"  Total Read Bytes: {disk_counters.read_bytes}")
print(f"  Total Write Bytes: {disk_counters.write_bytes}")
print(f"  Total Read Time: {disk_counters.read_time} ms")
print(f"  Total Write Time: {disk_counters.write_time} ms")

# Get network counters
network_counters = psutil.net_io_counters()
print("Network Counters:")
print(f"  Total Bytes Sent: {network_counters.bytes_sent}")
print(f"  Total Bytes Received: {network_counters.bytes_recv}")
print(f"  Total Packets Sent: {network_counters.packets_sent}")
print(f"  Total Packets Received: {network_counters.packets_recv}")
