from itertools import islice

class Fraction(object):

    """Docstring for Fraction. """

    def __init__(self,n,d):
        """This class will take numerator and denominator
        """
        self._n = n
        self._d = d

    @classmethod
    def factors(self, n):
        return sorted(set([int(n/x) for x in range(2,n) if int(n/x) > 1 and n%x == 0]))

    @classmethod
    def lcm(self, n):
        return min(self.factors(n))

    @classmethod
    def ucf(self, n1, n2):
        pass

    @classmethod
    def is_prime(self, n1):
        return all([n1 % x for x in range(2,n1)])

    @classmethod
    def get_primes(self):
        ctr = 1
        while True:
            if self.is_prime(ctr):
                yield ctr
            ctr += 1


    @classmethod
    def common_divisor(self, n1 ,n2):
        return set(self.factors(n1)) & set(self.factors(n2))



f = Fraction(2,3)
# print (f.factors(100))
# print (f.lcm(100))
# print (f.common_divisor(10,100))

# for x in range(50):
#     print(f.is_prime(x))

for x in islice(f.get_primes(),1,30):
    print(x)
