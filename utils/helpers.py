import socket
import os

def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def create_output_dir(target):
    path = f"output/{target}"
    os.makedirs(path, exist_ok=True)
    return path
