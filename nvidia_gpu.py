from pynvml import *

nvmlInit();

total_nvidia_gpu = nvmlDeviceGetCount()

for i in range(total_nvidia_gpu):
    GPU_ID = nvmlDeviceGetHandleByIndex(i)



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