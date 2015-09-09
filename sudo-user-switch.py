

import subprocess
import shlex
import getpass

print "The script was called by: " + getpass.getuser()

print "Now do something as root..."
so1 = subprocess.call(shlex.split('sudo /etc/init.d/docker status'))
print so1

print "Switching back to the calling user: " + getpass.getuser()



