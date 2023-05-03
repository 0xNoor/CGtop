import time
import os
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






while(1):
	os.system("clear");
	for i in BANNER:
		print(i);
	print(nvidia_gpu_name(0))
	print(nvidia_gpu_temp(GPU_ID))
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
