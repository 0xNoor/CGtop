import time
import os
import subprocess
import re


def radeon_gpu_usage(output):
    gpu_usage = re.search(r"gpu.+?([0-9.]+)", output).group(1)
    return gpu_usage

def radeon_gpu_vram_usage(output):
    vram = re.search(r"vram.+?([0-9.]+)", output).group(1)

def radeon_gpu_vram_mem(output):
    vram_mem = re.search(r'vram \d+\.\d+% (\d+\.\d+)mb', output).group(1)



'''
ee = re.search(r"ee.+?([0-9.]+)", output).group(1)
spi = re.search(r"spi.+?([0-9.]+)", output).group(1)
'''