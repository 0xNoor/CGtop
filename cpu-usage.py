import time
import os
try:
	import psutil;
except:
	print("psutil not installed");

num_cores = psutil.cpu_count(logical=True);

while True:
    cpu_percent = psutil.cpu_percent();
    per_cpu_percent = psutil.cpu_percent(percpu=True);
    for i in range(num_cores):
         print(f"Core ID {i+1} usage is {per_cpu_percent[i]}");
    print(f"CPU usage: {cpu_percent}%");
    time.sleep(1);
    print("\r")
#    os.system('clear');
    print(f"\033[F" * (num_cores+2), end="")
