import nmap
import os

from device import Device
from log import Log


log = Log()

def get_inet_address():
    """Get the network address to scan with nmap."""
    data = os.popen('ifconfig').read()
    wlan_index = data.find('wl')
    ip_a = None

    # If we're on a wireless network, extract the network address
    if wlan_index != -1:
        ip_a = data[wlan_index:]
        ip_a = ip_a[ip_a.index('inet '):ip_a.index('netmask')]
        ip_a = ip_a[5:ip_a.rindex('.')] + '.0/24'

    return ip_a

def get_devices():
    """Get a list of connected devices."""
    nmap_address = get_inet_address()
    devices = []

    if nmap_address:
        nm = nmap.PortScanner()
        try:
            nm.scan(nmap_address, arguments='-sP')['scan']

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


print(get_devices())