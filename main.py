from nvidia_gpu import *
from cpu_usage import *
from radeon_gpu2 import *

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

if "nvidia" in gpu_check:
	nvmlInit();
	for i in range(total_nvidia_gpu()):
		GPU_ID = nvmlDeviceGetHandleByIndex(i)
elif "amdgpu" in gpu_check:
	pass
else:
	pass


while(1):
	os.system("clear");
	for i in BANNER:
		print(i);
	cpu_usage();
	per_cpu_usage();
	per_cpu_freq();
	#time.sleep(1);


	if "nvidia" in gpu_check:
		print(nvidia_gpu_name(0))
		print(nvidia_gpu_temp(GPU_ID))
		print(nvidia_gpu_core_clock(GPU_ID))
		print(nvidia_gpu_mem_clock(GPU_ID))
		time.sleep(1)
	else:
		pass
	if "amdgpu" in gpu_check:
		print(amd_gpu_vram_usage(0))
		print(amd_gpu_core_clock(0))
		print(amd_gpu_mem_clock(0))


		"""radeon_out = subprocess.check_output("radeontop -l 1 -d -", shell=True)
		output = radeon_out.decode()
		print(radeon_gpu_usage(output))
		print(radeon_gpu_mem_freq(output))
		time.sleep(1)"""
	else:
		pass
	time.sleep(1)

