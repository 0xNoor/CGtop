from gpu_check import *
try:
    if "nvidia" in gpu_info:
        from pynvml import *
except:
    print("pynvml not installed")
    if "nvidia" in gpu_info:
        print("Trying to install Pynvml")
        import subprocess
        subprocess.call(['pip', 'install', 'pynvml' ])
finally:
    if "nvidia" in gpu_info:    
        from pynvml import *


def total_nvidia_gpu():
    return nvmlDeviceGetCount()

def nvidia_gpu_name(GPU_ID):
    return nvmlDeviceGetName(nvmlDeviceGetHandleByIndex(GPU_ID))

def nvidia_gpu_serial(GPU_ID):
    return nvmlDeviceGetSerial(GPU_ID)

def nvidia_gpu_core_clock(GPU_ID):
    return nvmlDeviceGetClockInfo(GPU_ID, 0)

def nvidia_gpu_mem_clock(GPU_ID):
    return nvmlDeviceGetClockInfo(GPU_ID, 2)

def nvidia_gpu_temp(GPU_ID):
    temp = nvmlDeviceGetTemperature(GPU_ID, 0)
    return temp

def nvidia_driver_ver():
    return nvmlSystemGetDriverVersion()

def nvidia_process_name(PID):
    process = nvmlSystemGetProcessName(PID)
    return process


'''
print(nvmlDeviceGetName(nvmlDeviceGetHandleByIndex(0)))
print(nvmlSystemGetDriverVersion())
print(nvmlDeviceGetTemperature(gpu_index, 0))
'''
