'''
This program will identify the blk device id 
'''
import subprocess

p1 = subprocess.Popen(['lsblk', '-d'], stdout=subprocess.PIPE)
output = p1.communicate()[0]

print '/'.join(['/dev', output.splitlines()[1].split()[0] + '4'])





