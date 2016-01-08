import subprocess

print 'Starting server.py'
p = subprocess.Popen('python server.py', shell=True)
retval = p.wait()
print 'Completing server.py'





