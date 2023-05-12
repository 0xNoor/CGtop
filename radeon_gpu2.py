try:
    from pyamdgpuinfo import *
except:
    print("pyamdgpuinfo not installed")

def total_amd_gpu(ID):
    return get_gpu(ID)

def amd_gpu_core_clock(ID):
    sclk = total_amd_gpu(ID).query_sclk()
    return sclk

def amd_gpu_mem_clock(ID):
    mclk =total_amd_gpu(ID).query_mclk()
    return mclk

def amd_gpu_vram_usage(ID):
    vram_usage = total_amd_gpu(ID).query_vram_usage()
    return vram_usage

def amd_gpu_gtt(ID):
    gtt = total_amd_gpu(ID).query_gtt_usage()
    return gtt

def amd_gpu_temp(ID):
    temp = total_amd_gpu(ID).query_temperature()
    return temp

