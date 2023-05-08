import time
import os
import subprocess
import re


def radeon_gpu_usage(output):
    gpu_usage = re.search(r"gpu.+?([0-9.]+)", output).group(1)
    return gpu_usage

def radeon_gpu_vram_usage(output):
    vram = re.search(r"vram.+?([0-9.]+)", output).group(1)
    return vram

def radeon_gpu_vram_mem(output):
    vram_mem = re.search(r'vram \d+\.\d+% (\d+\.\d+)mb', output).group(1)
    return vram_mem

def radeon_mem_clock(output):
    mem_clock_percent = re.search(r"mclk.+?([0-9.]+)", output).group(1)
    return mem_clock_percent

def radeon_shader_clock(output):
    shader_clock = re.search(r"sclk.+?([0-9.]+)", output).group(1)
    return shader_clock

def radeon_gpu_mem_freq(output):
    mem_clock_freq = re.search(r'mclk \d+\.\d+% (\d+\.\d+)ghz', output).group(1)
    return mem_clock_freq

def radeon_gpu_shader_freq(output):
    shader_clock_freq = re.search(r'sclk \d+\.\d+% (\d+\.\d+)ghz', output).group(1)
    return shader_clock_freq


'''
ee = re.search(r"ee.+?([0-9.]+)", output).group(1)
spi = re.search(r"spi.+?([0-9.]+)", output).group(1)
'''