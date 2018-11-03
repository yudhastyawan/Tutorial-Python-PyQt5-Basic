import sys
import os
import subprocess

# cmd = 'ping 8.8.8.8 -t'
cmd = 'pip list'
# a = subprocess.run(cmd,shell=True)
# print(str(a.returncode))
stdouterr = subprocess.Popen(cmd,stderr=subprocess.STDOUT,stdout=subprocess.PIPE)
print(str(stdouterr.communicate()[0].decode('utf-8')).split()[0])
