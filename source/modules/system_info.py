#!/usr/bin/python3

import psutil

def convert_bytes_to_gb_mb(value):
    if value < (1024 ** 2):
        return "{:.1f} MB".format(value / (1024 ** 2))
    else:
        return "{:.1f} GB".format(value / (1024 ** 3))

def print_cpu_info():
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


def print_memory_info():
    # a. Total, available and Percentage
    mem = psutil.virtual_memory()
    total_mem = mem.total
    available_mem = mem.available
    usage_percent = mem.percent

    print("Total Memory:", convert_bytes_to_gb_mb(total_mem))
    print("Available Memory:", convert_bytes_to_gb_mb(available_mem))

    print("Memory Usage (%):", usage_percent)

    # b. Swap information
    swap = psutil.swap_memory()
    print("Swap Memory:", convert_bytes_to_gb_mb(swap.total))

    # c. General Memory info
    mem_info = psutil.virtual_memory()
    print("Active Memory:", convert_bytes_to_gb_mb(mem_info.active))
    print("Inactive Memory:", convert_bytes_to_gb_mb(mem_info.inactive))
    print("Buffers:", convert_bytes_to_gb_mb(mem_info.buffers))
    print("Cached Memory:", convert_bytes_to_gb_mb(mem_info.cached))
    print("Shared Memory:", convert_bytes_to_gb_mb(mem_info.shared))


def print_disk_usage():
    # a. Monitors disk usage for ALL mounted partitions
    disk_usage = psutil.disk_usage('/')
    print("Disk Usage:", convert_bytes_to_gb_mb(disk_usage.used))

def print_system_info():
    # 1. CPU Usage
    print_cpu_info()

    # 2. Memory
    print_memory_info()

    # 3. Disk Usage
    print_disk_usage()

    # 4. Continue with the rest of the Python program
    print("Continuing with the rest of the program...")