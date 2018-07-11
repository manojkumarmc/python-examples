from itertools import islice

def tribi():
    a,b,c = 1,1,1
    yield a
    yield b
    yield c
    while True:
        d = a + b + c
        a = b
        b = c
        c = d
        yield d


for x in islice(tribi(), 10):
    print(x)
