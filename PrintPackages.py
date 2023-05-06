# file path is python -u C:\Users\sihoc\Documents\GitHub\OC-Hackathon-Voice-Converter\Test.py
import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
print(installed_packages)