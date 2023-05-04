from nvidia_gpu import *
from cpu_usage import *

BANNER =(
" ██████╗ ██████╗████████╗ ██████╗ ██████╗ ",
"██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗",
"██║     ██║  ███╗  ██║   ██║   ██║██████╔╝",
"██║     ██║   ██║  ██║   ██║   ██║██╔═══╝ ",
"╚██████╗╚██████╔╝  ██║   ╚██████╔╝██║     ",
" ╚═════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝     "
)

'''
gpu_check = subprocess.check_output("lspci -k | grep -A 2 -E '(VGA|3D)' | grep 'use' | awk '{print $NF}'", shell=True)
gpu_check = gpu_check.decode("utf-8").strip().split("\n")

if "nvidia" in gpu_check:
	nvmlInit();
	for i in range(total_nvidia_gpu()):
		GPU_ID = nvmlDeviceGetHandleByIndex(i)
else:
	pass
'''

while(1):
	os.system("clear");

	for i in BANNER:
		print(i);'''
	if "nvidia" in gpu_check:
		print(nvidia_gpu_name(0))
		print(nvidia_gpu_temp(GPU_ID))
		print(nvidia_gpu_core_clock(GPU_ID))
		print(nvidia_gpu_mem_clock(GPU_ID))
	else:
		pass'''
	cpu_usage();
	per_cpu_usage();
	per_cpu_freq();
	time.sleep(1);
