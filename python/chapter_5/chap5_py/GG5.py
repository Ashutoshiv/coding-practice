network_ips = ["192.168.1.1", "10.0.0.5", "89.29.00.0.2","349.23.0.00.2","23.34.09.02"]

for network in network_ips:
    print(f"Scanning IP: {network}...")

    if network == "192.168.1.1":
        print("WARNING: Root Server Found!")
    else:
        print("Scan clear")