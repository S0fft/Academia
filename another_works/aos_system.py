import psutil
import platform
 
my_system = platform.uname()
 
print(f"BIOS Version: {my_system.version}")
 
print(f"Machine: {my_system.machine}")
 
print(f"Processor: {my_system.processor}")
 
print(f"Memory SSD:{psutil.virtual_memory()}")
 
print(f"Memory RAM: {psutil.virtual_memory().total}")
 
# import igpu
# gpu_count = igpu.count_devices()
# gpu = igpu.get_device(0)
# print(f'This host has {gpu_count} devices.')
# print(f'The first gpu is a {gpu.name} with {gpu.memory.total:.0f}{gpu.memory.unit}.')
