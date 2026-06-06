import psutil

cpu = psutil.cpu_percent()

if cpu > 80:
    print("ALERT: CPU usage exceeded 80%")
else:
    print(f"CPU Usage: {cpu}%")