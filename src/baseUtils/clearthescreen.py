import platform
import subprocess

def clearscreen():
    cmd = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.run([cmd])

