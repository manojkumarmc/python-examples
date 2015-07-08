from itertools import islice

def factorial():
    n = 1
    num = 1
    while n >= 1:
        num = num * n
        n += 1
        yield num


f = factorial()

x = islice(f,2000)
print list(x)[1999]



