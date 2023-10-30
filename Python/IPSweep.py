import ipaddress
import subprocess 

def get_active_ips():
    """Returns a list of active IP addresses on the local network."""

    ips = []
    local_ip = ipaddress.ip_address(subprocess.check_output(["hostname", "-I"]).decode().strip())
    network = ipaddress.ip_network(local_ip.network_address + "/24")

    for ip in network:
        if ip != local_ip:
            ips.append(ip)

    return ips

if __name__ == "__main__":
    active_ips = get_active_ips()
    print("Active IP addresses on the local network:")
    for ip in active_ips:
        print(ip)
