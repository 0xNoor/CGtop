import time
import os
import subprocess
from nvidia_gpu import *
try:
	import psutil;
except:
	print("psutil not installed");




num_cores = psutil.cpu_count(logical=True);



def cpu_usage():
	cpu_percentage = psutil.cpu_percent();
	print(f"CPU Usage is : {cpu_percentage}%");

def per_cpu_usage():
	per_cpu_percentage = psutil.cpu_percent(percpu=True);
	for i in range(num_cores):
		print(f"Core ID {i+1} usage is {per_cpu_percentage[i]}");

BANNER =(
" ██████╗ ██████╗████████╗ ██████╗ ██████╗ ",
"██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗",
"██║     ██║  ███╗  ██║   ██║   ██║██████╔╝",
"██║     ██║   ██║  ██║   ██║   ██║██╔═══╝ ",
"╚██████╗╚██████╔╝  ██║   ╚██████╔╝██║     ",
" ╚═════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝     "
)





gpu_check = subprocess.check_output("lspci -k | grep -A 2 -E '(VGA|3D)' | grep 'use' | awk '{print $NF}'", shell=True)
gpu_check = gpu_check.decode("utf-8").strip().split("\n")



'''
gpu_check = subprocess.check_output("lspci -k | grep -A 2 -E '(VGA|3D)'", shell=True)
gpu_check = gpu_check.decode("utf-8").strip().split("\n")

print(len(gpu_check))

for i in range(len(gpu_check)):
    if "Kernel driver in use" in gpu_check[i]:
        gpu_driver = gpu_check[i]
        print(len(gpu_driver))
'''

if "nvidia" in gpu_check:
	nvmlInit();
	for i in range(total_nvidia_gpu()):
		GPU_ID = nvmlDeviceGetHandleByIndex(i)
else:
	pass




while(1):
	os.system("clear");

	for i in BANNER:
		print(i);
	if "nvidia" in gpu_check:
		print(nvidia_gpu_name(0))
		print(nvidia_gpu_temp(GPU_ID))
		print(nvidia_gpu_core_clock(GPU_ID))
		print(nvidia_gpu_mem_clock(GPU_ID))
	else:
		pass
	cpu_usage();
	per_cpu_usage();
	time.sleep(1);


#while True:
#	cpu_percent = psutil.cpu_percent();
#	per_cpu_percent = psutil.cpu_percent(percpu=True);
#	for i in range(num_cores):
#		print(f"Core ID {i+1} usage is {per_cpu_percent[i]}");
#	print(f"CPU usage: {cpu_percent}%");
#	time.sleep(1);
#	print(f"\033[F" * (num_cores+2), end="")
