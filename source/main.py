import psutil
# Number of CPU cores
num_cores = psutil.cpu_count()

# CPU frequency
cpu_freq = psutil.cpu_freq()
current_freq = cpu_freq.current
min_freq = cpu_freq.min
max_freq = cpu_freq.max

# CPU states
cpu_states = psutil.cpu_stats()

# CPU load
cpu_load = psutil.getloadavg()

print("Number of CPU cores:", num_cores)
print("Current CPU frequency (MHz):", current_freq)
print("Minimum CPU frequency (MHz):", min_freq)
print("Maximum CPU frequency (MHz):", max_freq)
print("CPU states:", cpu_states)
print("CPU load (1 min, 5 min, 15 min):", cpu_load)
