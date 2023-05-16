import time
import os
import subprocess
try:
	import psutil;
except:
	print("psutil not installed");
	print("Trying to install psutil")
	import subprocess
	subprocess.call(['pip', 'install', 'psutil' ])
finally:
	import psutil;

num_cores = psutil.cpu_count(logical=True);

def cpu_usage():
	cpu_percentage = psutil.cpu_percent();
	print(f"CPU Usage is : {cpu_percentage}%");

def per_cpu_usage():
	per_cpu_percentage = psutil.cpu_percent(percpu=True);
	for i in range(num_cores):
		print(f"Core ID {i+1} usage is {per_cpu_percentage[i]}");

def per_cpu_freq():
	per_cpu_frequency = psutil.cpu_freq();
	print(f"Core ID Frequency is {per_cpu_frequency}")






'''
gpu_check = subprocess.check_output("lspci -k | grep -A 2 -E '(VGA|3D)'", shell=True)
gpu_check = gpu_check.decode("utf-8").strip().split("\n")

print(len(gpu_check))

for i in range(len(gpu_check)):
    if "Kernel driver in use" in gpu_check[i]:
        gpu_driver = gpu_check[i]
        print(len(gpu_driver))
'''







#while True:
#	cpu_percent = psutil.cpu_percent();
#	per_cpu_percent = psutil.cpu_percent(percpu=True);
#	for i in range(num_cores):
#		print(f"Core ID {i+1} usage is {per_cpu_percent[i]}");
#	print(f"CPU usage: {cpu_percent}%");
#	time.sleep(1);
#	print(f"\033[F" * (num_cores+2), end="")
