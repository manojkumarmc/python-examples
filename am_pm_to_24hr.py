import sys

time = raw_input().strip()

if time[-2:] == 'PM':
    print str(int(time[0:2]) + 12) + time[2:len(time) - 2]
else:
    print time.replace('PM').replace('AM')
