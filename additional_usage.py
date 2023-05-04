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
