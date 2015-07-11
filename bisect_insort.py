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


