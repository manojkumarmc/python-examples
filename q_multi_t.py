from Queue import Queue
from threading import Thread, current_thread

def do_stuff(q):
  while True:
    print threading.current_thread().name
    print "\n Processing " + str(q.get())
    q.task_done()

q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(name="Thread" + str(i), target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

for x in range(100):
  q.put(x)

q.join()
