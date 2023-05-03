from pynvml import *

nvmlInit();

total_nvidia_gpu = nvmlDeviceGetCount()

for i in range(total_nvidia_gpu):
    GPU_ID = nvmlDeviceGetHandleByIndex(i)



def nvidia_gpu_name(GPU_ID):
    name = nvmlDeviceGetName(nvmlDeviceGetHandleByIndex(GPU_ID))
    return name

def nvidia_gpu_temp(GPU_ID):
    temp = nvmlDeviceGetTemperature(GPU_ID, 0)
    return temp




'''
print(nvmlDeviceGetName(nvmlDeviceGetHandleByIndex(0)))
print(nvmlSystemGetDriverVersion())
print(nvmlDeviceGetTemperature(gpu_index, 0))
'''