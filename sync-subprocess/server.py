import subprocess
import sys


print 'Calling script'
p = subprocess.Popen('./echoer.sh', shell=True, stderr=subprocess.STDOUT)
retval = p.wait()
print 'Finished script'

sys.exit(0)
