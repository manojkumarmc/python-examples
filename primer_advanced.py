
from itertools import islice

def is_prime(n):
    return all(n % x for x in xrange(2,n))

def prime_gen():
    ret_val = 1
    while True:
        if is_prime(ret_val):
            yield ret_val
        ret_val += 1

# print 100 prime numbers
sum_prime = 0
for x in islice(prime_gen(), 0, 100):
    print x
    sum_prime += x
    

print '*' * 50
print 'The sum is %s ' % sum_prime



