import Queue
import random

q = Queue.Queue()
lst = []

for x in xrange(10):
    val = random.randint(1, 100)
    q.put(val)
    lst.append(val)

for i in lst:
    print i
    
print "===================="

while not q.empty():
    print q.get()
    
    


