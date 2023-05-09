try:
    from pyamdgpuinfo import *
except:
    print("pyamdgpuinfo not installed")

def total_amd_gpu(ID):
    return get_gpu(ID)

def amd(ID):
    sclk = total_amd_gpu(ID)
    s = sclk.query_sclk()
    return s

print(amd(0))