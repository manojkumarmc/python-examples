
from itertools import islice

def is_prime(a):
    return all(a % i for i in xrange(2, a))

def prime_summer(n):
    sum = 0
    for x in xrange(1,n):
        if is_prime(x):
            sum += x
    return sum

def prime_lister(n):
    for x in xrange(n):
        if is_prime(x):
            print x

#print prime_summer(100)

prime_lister(100)

    
