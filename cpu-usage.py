import time
try:
	import psutil;
except:
	print("psutil not installed");


while True:
    cpu_percent = psutil.cpu_percent();
    print(f"CPU usage: {cpu_percent}%", end="\r");
    time.sleep(1);
