import time

"""
This is a prgram to check the debugging of python code in production
"""

# usage : gdb python <pid of running process>
#
# Get C stack trace : ( gdb ) bt
# Get Python stack  : ( gdb ) py-bt
# Get hung process  : ( gdb ) info threads
# Get python  info  : ( gdb ) py-list

auto_summer = 0

while True:
    time.sleep(1)
    print ( auto_summer )
    auto_summer += 1
