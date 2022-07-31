import os

from pushbullet import PushBullet


CONFIG_FILE = 'notifications.config'


class NotificationManager:
    """Manage notifications."""

    def __init__(self):
        """Create the manager."""
        self._api_key = None

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                self._api_key = f.read().strip()

        if not self._api_key:
            self._api_key = input('Enter PushBullet API key: ')

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            f.write(self._api_key)

        self._pb = PushBullet(self._api_key)

    def push(self, title, message):
        """Send a notification."""
        self._pb.push_note(title, message)
