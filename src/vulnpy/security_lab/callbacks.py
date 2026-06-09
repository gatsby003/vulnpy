from urllib.parse import urljoin
from urllib.request import urlopen


CALLBACK_BASE_URL = "https://example.com/callbacks/"


def fetch_callback_preview(callback_path):
    target_url = urljoin(CALLBACK_BASE_URL, callback_path)
    with urlopen(target_url, timeout=5) as response:
        return response.read(2048).decode("utf-8", "replace")


def fetch_absolute_callback(callback_url):
    with urlopen(callback_url, timeout=5) as response:
        return response.read(2048).decode("utf-8", "replace")
