
from Queue import Queue
from threading import Thread
import time

NUM_OF_FLOORS = 4
NUM_OF_ELEVS  = 2

def worker():
    current_floor = 0
    in_process = False    
    while True:
        if not in_process:
            dest = q.get()
        print '\n The floor being processed is ' + str(dest)

        if int(dest) > current_floor:
            while current_floor < int(dest):
                in_process = True
                time.sleep(1)
                current_floor += 1
                print '\nAt level: ' + str(current_floor)
        elif int(dest) < current_floor:
            while current_floor > int(dest):
                in_process = True
                time.sleep(1)
                current_floor -= 1
                print '\nAt level: ' + str(current_floor)

        in_process = False
        q.task_done()


def multi_worker(elev_name=''):
    current_floor = 0
    in_process = False    
    while True:
        if not in_process:
            dest = q.get()
        print '\n'+ elev_name +' | Destination : ' + str(dest)

        if int(dest) > current_floor:
            while current_floor < int(dest):
                in_process = True
                time.sleep(1)
                current_floor += 1
		print '\n'+ elev_name +' | At level: ' + str(current_floor)
		if current_floor in lst:
		    print '\n'+ elev_name +' | Opening door at :' + str(current_floor)
                    time.sleep(1)
		    print '\n'+ elev_name +' | Closing door at :' + str(current_floor)
		    filter(lambda a: a != current_floor, lst)	
                
        elif int(dest) < current_floor:
            while current_floor > int(dest):
                in_process = True
                time.sleep(1)
                current_floor -= 1
                print '\n'+ elev_name +' | At level: ' + str(current_floor)
		if current_floor in lst:
		    print '\n'+ elev_name +' | Opening door at :' + str(current_floor)
                    time.sleep(1)
		    print '\n'+ elev_name +' | Closing door at :' + str(current_floor)
		    filter(lambda a: a != current_floor, lst)	

        in_process = False
        q.task_done()    


q = Queue()
lst = []
for elev in xrange(NUM_OF_ELEVS):
    t = Thread(target=multi_worker, args=('Elev-' + str(elev + 1),))
    t.daemon = True
    t.start()

while True:
    level = raw_input('\nPlease enter your level: ')
    q.put(level)
    lst.append(int(level))

q.join()

'''
The program can be run using : 
==============================

user@hostname: $ python server.py

Sample output:
=============
Please enter your level: 5

Please enter your level: 
Elev-1 | Destination : 5

Elev-1 | At level: 1
5

Please enter your level: 
Elev-2 | Destination : 5

Elev-1 | At level: 2

Elev-2 | At level: 1

Elev-1 | At level: 3

Elev-2 | At level: 2

Elev-1 | At level: 4

Elev-2 | At level: 3

Elev-1 | At level: 5

Elev-1 | Opening door at :5

Elev-2 | At level: 4

Elev-1 | Closing door at :5

Elev-2 | At level: 5

Elev-2 | Opening door at :5

Elev-2 | Closing door at :5

'''


