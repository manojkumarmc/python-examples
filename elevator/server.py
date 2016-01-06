
from Queue import Queue
from threading import Thread
import time

NUM_OF_FLOORS = 4
NUM_OF_ELEVS  = 1

def worker():
    current_floor = 0
    in_process = False    
    while True:
        if not in_process:
            dest = q.get()
        print "\n The floor being processed is " + str(dest)

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


q = Queue()

t = Thread(target=worker)
t.daemon = True
t.start()


while True:
    level = raw_input("\nPlease enter your level: ")
    q.put(level)

q.join()


