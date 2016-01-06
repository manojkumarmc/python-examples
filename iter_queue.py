import Queue

class IterableQueue():
    def __init__(self,source_queue):
            self.source_queue = source_queue
    def __iter__(self):
    	while True:
            try:
               yield self.source_queue.get_nowait()
            except Queue.Empty:
               return


q = Queue.Queue()
q.put(1)
q.put(2)
q.put(3)

for n in IterableQueue(q):
    print n

while not q.empty():
    print q.get()
