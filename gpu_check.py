import subprocess

gpu_info = subprocess.check_output("lspci -k | grep -A 2 -E '(VGA|3D)' | grep 'use' | awk '{print $NF}'", shell=True)
gpu_info = gpu_info.decode("utf-8").strip().split("\n")

