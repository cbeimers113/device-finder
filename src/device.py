class Device:
    """Encapsulate device data."""

    def __init__(self, device_name, mac_address, ip_address, manufacturer):
        """ Initialize a device."""
        self._device_name = device_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._manufacturer = manufacturer

    def get_device_name(self):
        """Get the device's name."""
        return self._device_name

    def get_mac_address(self):
        """Get the device's MAC address."""
        return self._mac_address

    def get_ip_address(self):
        """Get the device's IP address."""
        return self._ip_address

    def get_manufacturer(self):
        """Get the device's manufacturer."""
        return self._manufacturer

    def __eq__(self, other):
        """Equality comparison."""
        return self._device_name == other._device_name and \
            self._mac_address == other._mac_address and \
            self._ip_address == other._ip_address and \
            self._manufacturer == other._manufacturer

    def __gt__(self, other):
        """Greater than comparison, compare IP address."""
        return self._ip_address > other._ip_address

    def __lt__(self, other):
        """Less than comparison, compare IP address."""
        return self._ip_address < other._ip_address

    def __ge__(self, other):
        """Greater than or equal to comparison."""
        return self > other or self == other

    def __le__(self, other):
        """Less than or equal to comparison."""
        return self < other or self == other

    def __str__(self):
        return f'Name: {self._device_name}\nMAC address: {self._mac_address}\nIP address: {self._ip_address}\nManufacturer: {self._manufacturer}'
