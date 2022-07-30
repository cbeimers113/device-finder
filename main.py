import nmap
import os
import socket

from device import Device
from log import Log


log = Log()


def get_inet_address():
    """Get the network address to scan with nmap."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_a = s.getsockname()[0]
    ip_a = ip_a[:ip_a.rindex('.')] + '.0/24'
    s.close()

    return ip_a


def get_devices():
    """Get a list of connected devices."""
    inet_address = get_inet_address()
    print(inet_address)
    devices = []

    if inet_address:
        nm = nmap.PortScanner()
        try:
            nm.scan(inet_address, arguments='-sP')['scan']

            # Load devices that are on the network
            for ip_address in nm.all_hosts():
                hosts = nm[ip_address]
                device_name = hosts['hostnames'][0]['name']
                mac_address = "-"
                manufacturer = "-"

                if 'mac' in hosts['addresses']:
                    mac_address = hosts['addresses']['mac']

                    if mac_address in hosts['vendor']:
                        manufacturer = hosts['vendor'][mac_address]

                devices.append(
                    Device(device_name, mac_address,
                           ip_address, manufacturer)
                )

        # Catch any errors with nmap
        except Exception as e:
            log.error('An error occured with nmap:')
            log.no_prefix(e)

    return devices


for device in get_devices():
    print(f'{device}\n')
