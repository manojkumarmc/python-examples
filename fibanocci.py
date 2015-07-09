from itertools import islice

def fib():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        a,b = b, a+b
        yield b

output = islice(fib(), 0, 100)

for o in output:
    print o

    
