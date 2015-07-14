import bisect
import random
from itertools import islice

def gen_numbers():
    while True:
        yield random.randint(1,100000)

output = []
for x in islice(gen_numbers(), 1,10):
    bisect.insort(output, x)
    
print output

output1 = []
def gen_tuples():
    while True:
        yield (random.randint(1,100), random.randint(1,10000))

for y in islice(gen_tuples(), 1,10):
    bisect.insort(output1, y[0])

print "=" * 30
print output1

