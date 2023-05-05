import time
import os
import subprocess
import re

radeon_out = subprocess.check_output("radeontop -l 1 -d -", shell=True)
output = radeon_out.decode()
gpu_usage = re.search(r"gpu.+?([0-9.]+)", output).group(1)

vram = re.search(r"vram.+?([0-9.]+)", output).group(1)
vram_mem = re.search(r'vram \d+\.\d+% (\d+\.\d+)mb', output)
vram_mb = vram_mem.group(1)
print(f"GPU: {gpu_usage}, vram: {vram}, vram-mem {vram_mb}")


'''
ee = re.search(r"ee.+?([0-9.]+)", output).group(1)
spi = re.search(r"spi.+?([0-9.]+)", output).group(1)
'''