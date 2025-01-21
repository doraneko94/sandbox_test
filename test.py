import socket

class BlockedSocket:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Network access is disabled")

socket.socket = BlockedSocket

try:
    import requests
    print(requests.get("http://example.com"))
except Exception as e:
    print(f"Network exception: {e}")