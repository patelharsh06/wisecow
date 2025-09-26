import psutil

def check_cpu_usage(threshold=80):
    cpu = psutil.cpu_percent(interval=1)
    if cpu > threshold:
        print(f"ALERT: High CPU usage! Current usage: {cpu}%")
    else:
        print(f"CPU usage is normal at {cpu}%")

def check_memory_usage(threshold=80):
    mem = psutil.virtual_memory()
    if mem.percent > threshold:
        print(f"ALERT: High memory usage! Current usage: {mem.percent}%")
    else:
        print(f"Memory usage is normal at {mem.percent}%")

def check_disk_usage(threshold=80):
    disk = psutil.disk_usage('/')
    if disk.percent > threshold:
        print(f"ALERT: High disk usage! Current usage: {disk.percent}%")
    else:
        print(f"Disk usage is normal at {disk.percent}%")

def check_process_count(max_processes=300):
    processes = len(psutil.pids())
    if processes > max_processes:
        print(f"ALERT: High number of processes! Current count: {processes}")
    else:
        print(f"Process count is normal at {processes}")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_process_count()
