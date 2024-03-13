#!/usr/bin/python3
import psutil

# 1. CPU Usage
# a. Cores
num_cores = psutil.cpu_count()
print("Number of Cores:", num_cores)

# b. Frequency
freq = psutil.cpu_freq()
print("Current Frequency (MHz):", freq.current)
print("Minimum Frequency (MHz):", freq.min)
print("Maximum Frequency (MHz):", freq.max)

# c. States
states = psutil.cpu_stats()
print("CPU States:", states)

# d. Load
load_avg = psutil.getloadavg()
print("Average System Load (1 min, 5 min, 15 min):", load_avg)

# 2. Memory
# a. Total, available and Percentage
mem = psutil.virtual_memory()
print("Total Memory (bytes):", mem.total)
print("Available Memory (bytes):", mem.available)
print("Memory Usage (%):", mem.percent)

# b. Swap information
swap = psutil.swap_memory()
print("Swap Memory (bytes):", swap.total)

# c. General Memory info
mem_info = psutil.virtual_memory()
print("Active Memory (bytes):", mem_info.active)
print("Inactive Memory (bytes):", mem_info.inactive)
print("Buffers (bytes):", mem_info.buffers)
print("Cached (bytes):", mem_info.cached)
print("Shared Memory (bytes):", mem_info.shared)

# 3. Disk Usage
# a. Monitors disk usage for ALL mounted partitions
disk_usage = psutil.disk_usage('/')
print("Disk Usage (bytes):", disk_usage.total)


# d. Continue with the rest of the Python program
print("Continuing with the rest of the program...")