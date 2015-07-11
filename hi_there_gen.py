
from itertools import islice

def linked_in_generator():
    ctr = 1
    while ctr >= 1:
        if ctr % 4 == 0 and ctr % 6 == 0:
            yield "HiThere"
        elif ctr % 6 == 0 and ctr % 4 != 0:
            yield "There"
        else:
            yield "Hi"
        ctr += 1

input = 100

for x in islice(linked_in_generator(),1,100):
    print x

