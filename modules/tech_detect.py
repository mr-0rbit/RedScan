import subprocess

def run(target):
    try:
        return subprocess.getoutput(f"whatweb {target}")
    except:
        return None
