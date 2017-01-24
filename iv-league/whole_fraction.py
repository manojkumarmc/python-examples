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
    def lcf(self, n):
        return min(self.factors(n))

    @classmethod
    def common_divisor(self, n1 ,n2):
        return set(self.factors(n1)) & set(self.factors(n2))



f = Fraction(2,3)
print (f.factors(100))
print (f.lcf(100))
print (f.common_divisor(10,100))

